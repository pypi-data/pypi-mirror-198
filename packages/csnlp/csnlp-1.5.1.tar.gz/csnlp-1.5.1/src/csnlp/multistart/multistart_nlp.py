from functools import lru_cache, partial
from itertools import repeat
from typing import (
    Any,
    ClassVar,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Literal,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

import casadi as cs
import numpy as np
import numpy.typing as npt
from joblib import Parallel, delayed

from csnlp.core.cache import invalidate_cache
from csnlp.core.solutions import Solution, subsevalf
from csnlp.nlps.nlp import Nlp
from csnlp.nlps.objective import _solve_and_get_stats

SymType = TypeVar("SymType", cs.SX, cs.MX)


def _n(sym_name: str, scenario: int) -> str:
    """Internal utility for the naming convention of i-scenario's symbols."""
    return f"{sym_name}__{scenario}"


def _get_value(x, sol: Solution[SymType], old, new, eval: bool = True):
    """Internal utility for substituting numerical values in solutions."""
    return sol._get_value(
        cs.substitute(x, old, new), eval=eval  # type: ignore[call-arg]
    )


class MultistartNlp(Nlp[SymType], Generic[SymType]):
    """Base class for NLP with multistarting."""

    __slots__ = ("_starts",)
    is_multi: ClassVar[bool] = True

    def __init__(self, *args, starts: int, **kwargs) -> None:
        """Initializes the multistart NLP instance.

        Parameters
        ----------
        args, kwargs
            See inherited `csnlp.Nlp`.
        starts : int
            A positive integer for the number of multiple starting guesses to optimize.

        Raises
        ------
        ValueError
            Raises if the scenario number is invalid.
        """
        if starts <= 0:
            raise ValueError("Number of scenarios must be positive and > 0.")
        super().__init__(*args, **kwargs)
        self._starts = starts

    @property
    def starts(self) -> int:
        """Gets the number of starts."""
        return self._starts

    def solve_multi(
        self,
        pars: Union[
            None, Dict[str, npt.ArrayLike], Iterable[Dict[str, npt.ArrayLike]]
        ] = None,
        vals0: Union[
            None, Dict[str, npt.ArrayLike], Iterable[Dict[str, npt.ArrayLike]]
        ] = None,
        return_all_sols: bool = False,
        **_,
    ) -> Union[Solution[SymType], List[Solution[SymType]]]:
        """Solves the NLP with multiple initial conditions.

        Parameters
        ----------
        pars : dict[str, array_like] or iterable of, optional
            An iterable that, for each multistart, contains a dictionary with, for each
            parameter in the NLP scheme, the corresponding numerical value. In case a
            single dict is passed, the same is used across all scenarions. Can be `None`
            if no parameters are present.
        vals0 : dict[str, array_like] or iterable of, optional
            An iterable that, for each multistart, contains a dictionary with, for each
            variable in the NLP scheme, the corresponding initial guess. In case a
            single dict is passed, the same is used across all scenarions. By default
            `None`, in which case  initial guesses are not passed to the solver.
        return_all_sols : bool, optional
            If `True`, returns the solution of each multistart of the NLP; otherwise,
            only the best solution is returned. By default, `False`.

        Returns
        -------
        Solution or list of Solutions
            Depending on the flags `return_all_sols`, returns
             - the best solution out of all multiple starts
             - all the solutions (one per start)
        """
        raise NotImplementedError


class StackedMultistartNlp(MultistartNlp[SymType], Generic[SymType]):
    """A class that models and solves an NLP from multiple starting initial guesses by
    automatically stacking the problem multiple independent times in the same,
    larger-scale NLP. This allows to solve the original problem multiple times via a
    single call to the solver."""

    __slots__ = ("_stacked_nlp", "_fs")

    def __init__(self, *args, starts: int, **kwargs) -> None:
        # this class essentially is a facade that hides an internal nlp in which the
        # problem (variables, parameters, etc.) are duplicated by the requested number
        # of multiple starts. For this reason, all methods are overridden to create
        # multiples of these in the hidden nlp.
        super().__init__(*args, starts=starts, **kwargs)
        self._stacked_nlp = Nlp(*args, **kwargs)  # actual nlp

    @lru_cache
    def _symbols(
        self,
        i: Optional[int] = None,
        vars: bool = False,
        pars: bool = False,
        dual: bool = False,
    ) -> Dict[str, SymType]:
        """Internal utility to retrieve the symbols of the i-th scenario."""
        nlp = self._stacked_nlp.unwrapped
        S: Dict[str, SymType] = {}
        if vars:
            S.update(
                self._vars
                if i is None
                else {k: nlp._vars[_n(k, i)] for k in self._vars}
            )
        if pars:
            S.update(
                self._pars
                if i is None
                else {k: nlp._pars[_n(k, i)] for k in self._pars}
            )
        if dual:
            S.update(
                self._dual_vars
                if i is None
                else {k: nlp._dual_vars[_n(k, i)] for k in self._dual_vars}
            )
        return S

    @invalidate_cache(_symbols)
    def parameter(self, name: str, shape: Tuple[int, int] = (1, 1)) -> SymType:
        out = super().parameter(name, shape)
        for i in range(self._starts):
            self._stacked_nlp.parameter(_n(name, i), shape)
        return out

    @invalidate_cache(_symbols)
    def variable(
        self,
        name: str,
        shape: Tuple[int, int] = (1, 1),
        lb: Union[npt.ArrayLike, cs.DM] = -np.inf,
        ub: Union[npt.ArrayLike, cs.DM] = +np.inf,
    ) -> Tuple[SymType, SymType, SymType]:
        out = super().variable(name, shape, lb, ub)
        for i in range(self._starts):
            self._stacked_nlp.variable(_n(name, i), shape, lb, ub)
        return out

    @invalidate_cache(_symbols)
    def constraint(
        self,
        name: str,
        lhs: Union[SymType, np.ndarray, cs.DM],
        op: Literal["==", ">=", "<="],
        rhs: Union[SymType, np.ndarray, cs.DM],
        soft: bool = False,
        simplify: bool = True,
    ) -> Tuple[SymType, ...]:
        expr = lhs - rhs
        if simplify:
            expr = cs.simplify(expr)
        out = super().constraint(name, expr, op, 0, soft, False)

        symbols = self._symbols(vars=True, pars=True)
        for i in range(self._starts):
            symbols_i = self._symbols(i, vars=True, pars=True)
            expr_i = subsevalf(expr, symbols, symbols_i, eval=False)
            self._stacked_nlp.constraint(_n(name, i), expr_i, op, 0, soft, False)
        return out

    def minimize(self, objective: SymType) -> None:
        out = super().minimize(objective)
        symbols = self._symbols(vars=True, pars=True)
        self._fs: List[SymType] = [
            subsevalf(
                objective, symbols, self._symbols(i, vars=True, pars=True), eval=False
            )
            for i in range(self._starts)
        ]
        self._stacked_nlp.minimize(sum(self._fs))
        return out

    def init_solver(
        self,
        opts: Optional[Dict[str, Any]] = None,
        solver: Literal["opti", "qp"] = "opti",
    ) -> None:
        out = super().init_solver(opts, solver)
        self._stacked_nlp.init_solver(opts, solver)
        return out

    def solve_multi(
        self,
        pars: Union[
            None, Dict[str, npt.ArrayLike], Iterable[Dict[str, npt.ArrayLike]]
        ] = None,
        vals0: Union[
            None, Dict[str, npt.ArrayLike], Iterable[Dict[str, npt.ArrayLike]]
        ] = None,
        return_all_sols: bool = False,
        return_stacked_sol: bool = False,
        **_,
    ) -> Union[Solution[SymType], List[Solution[SymType]]]:
        assert not (
            return_stacked_sol and return_all_sols
        ), "`return_all_sols` and `return_stacked_sol` can't be both true."
        if pars is not None:
            pars_iter = repeat(pars, self.starts) if isinstance(pars, dict) else pars
            pars = {
                _n(n, i): pars_i[n]
                for i, pars_i in enumerate(pars_iter)
                for n in pars_i.keys()
            }
        if vals0 is not None:
            v0_iter = repeat(vals0, self.starts) if isinstance(vals0, dict) else vals0
            vals0 = {
                _n(n, i): vals0_i[n]
                for i, vals0_i in enumerate(v0_iter)
                for n in vals0_i.keys()
            }
        multi_sol = self._stacked_nlp.solve(pars, vals0)
        if return_stacked_sol:
            return multi_sol

        vars = self.variables
        symbols = self._symbols(vars=True, pars=True, dual=True)
        old = cs.vertcat(
            self._p, self._x, self._lam_g, self._lam_h, self._lam_lbx, self._lam_ubx
        )

        sols: List[Solution[SymType]] = []
        fs = [float(multi_sol.value(f)) for f in self._fs]
        idx = range(self._starts) if return_all_sols else (np.argmin(fs),)
        for i in idx:
            vals = {
                n: multi_sol.vals[_n(n, i)]  # type: ignore[arg-type]
                for n in vars.keys()
            }
            symbols_i = self._symbols(i, vars=True, pars=True, dual=True)
            new = subsevalf(old, symbols, symbols_i, False)
            get_value = partial(_get_value, sol=multi_sol, old=old, new=new)
            sols.append(
                Solution(
                    fs[i],  # type: ignore[call-overload]
                    vars,
                    vals,
                    multi_sol.stats,
                    get_value,
                )
            )
        return sols if return_all_sols else sols[0]

    def __call__(self, *args, **kwargs):
        return self.solve_multi(*args, **kwargs)


class ParallelMultistartNlp(MultistartNlp[SymType], Generic[SymType]):
    """A class that solves an NLP via parallelization of the computations."""

    __slots__ = ("_parallel", "_n_jobs")

    def __init__(
        self, *args, starts: int, n_jobs: Optional[int] = None, **kwargs
    ) -> None:
        """Initializes the multistart NLP instance.

        Parameters
        ----------
        args, kwargs
            See inherited `csnlp.Nlp`.
        starts : int
            A positive integer for the number of multiple starting guesses to optimize.
        n_jobs : int, optional
            Number of concurrently running jobs; see `n_job` in `joblib.Parallel`.

        Raises
        ------
        ValueError
            Raises if the scenario number is invalid.
        """
        super().__init__(*args, starts=starts, **kwargs)
        self._n_jobs = n_jobs
        self._parallel = Parallel(n_jobs=n_jobs)
        self.initialize_parallel()

    def initialize_parallel(self) -> None:
        """Initializes the parallel backend."""
        self._parallel.__enter__()

    def terminate_parallel(self) -> None:
        """Terminates the parallel backend."""
        self._parallel.__exit__(None, None, None)

    def solve_multi(
        self,
        pars: Union[
            None, Dict[str, npt.ArrayLike], Iterable[Dict[str, npt.ArrayLike]]
        ] = None,
        vals0: Union[
            None, Dict[str, npt.ArrayLike], Iterable[Dict[str, npt.ArrayLike]]
        ] = None,
        return_all_sols: bool = False,
        **_,
    ) -> Union[Solution[SymType], List[Solution[SymType]]]:
        if self._solver is None:
            raise RuntimeError("Solver uninitialized.")
        shared_kwargs = {
            "lbx": self._lbx,
            "ubx": self._ubx,
            "lbg": np.concatenate((np.zeros(self.ng), np.full(self.nh, -np.inf))),
            "ubg": 0,
        }
        pars_iter = (
            repeat(pars, self.starts)
            if pars is None or isinstance(pars, dict)
            else pars
        )
        vals0_iter = (
            repeat(vals0, self.starts)
            if vals0 is None or isinstance(vals0, dict)
            else vals0
        )
        kwargs = (
            self._process_pars_and_vals0(shared_kwargs.copy(), p, v0)
            for p, v0 in zip(pars_iter, vals0_iter)
        )
        sols: Iterator[Solution] = map(
            self._process_solver_sol,
            self._parallel(
                delayed(_solve_and_get_stats)(self._solver, kw) for kw in kwargs
            ),
        )
        if return_all_sols:
            return list(sols)

        # pick the best solution, with priority to successful solutions
        best_sol = next(sols)
        self._failures += not best_sol.success
        for sol in sols:
            if (not best_sol.success and sol.success) or (
                best_sol.success == sol.success and sol.f < best_sol.f
            ):
                best_sol = sol
            self._failures += not sol.success
        return best_sol

    def __getstate__(
        self,
        fullstate: bool = False,
    ) -> Union[None, Dict[str, Any], Tuple[Optional[Dict[str, Any]], Dict[str, Any]]]:
        # joblib.Parallel cannot be pickled or deepcopied
        state = super().__getstate__(fullstate)
        state[1].pop("_parallel", None)  # type: ignore[index]
        return state

    def __setstate__(
        self,
        state: Union[
            None, Dict[str, Any], Tuple[Optional[Dict[str, Any]], Dict[str, Any]]
        ],
    ) -> None:
        if isinstance(state, tuple) and len(state) == 2:
            state, slotstate = state
        else:
            slotstate = None
        if state is not None:
            self.__dict__.update(state)  # type: ignore[arg-type]
        if slotstate is not None:
            for key, value in slotstate.items():
                setattr(self, key, value)

        # re-initialized joblib.Parallel
        if not hasattr(self, "_n_jobs"):
            self._n_jobs = None
        self._parallel = Parallel(n_jobs=self._n_jobs)
        self.initialize_parallel()
