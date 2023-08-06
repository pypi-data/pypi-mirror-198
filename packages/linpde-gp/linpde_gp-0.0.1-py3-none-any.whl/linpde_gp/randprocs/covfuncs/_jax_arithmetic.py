import functools
import operator
from typing import Optional

from jax import numpy as jnp
import numpy as np
from probnum.randprocs.covfuncs._arithmetic_fallbacks import (
    ScaledCovarianceFunction,
    SumCovarianceFunction,
)
from probnum.typing import ArrayLike, ScalarLike, ScalarType

from ... import linfuncops
from ._jax import JaxCovarianceFunction, JaxCovarianceFunctionMixin


class JaxScaledCovarianceFunction(JaxCovarianceFunctionMixin, ScaledCovarianceFunction):
    def __init__(self, covfunc: JaxCovarianceFunction, scalar: ScalarLike) -> None:
        if not isinstance(covfunc, JaxCovarianceFunctionMixin):
            raise TypeError()

        super().__init__(covfunc, scalar)

    @property
    def scalar(self) -> ScalarType:
        return self._scalar

    @property
    def covfunc(self) -> JaxCovarianceFunction:
        return self._covfunc

    def _evaluate_jax(self, x0: jnp.ndarray, x1: Optional[jnp.ndarray]) -> jnp.ndarray:
        return self._scalar * self.covfunc.jax(x0, x1)

    def __rmul__(self, other: ArrayLike) -> JaxCovarianceFunction:
        if np.ndim(other) == 0:
            return JaxScaledCovarianceFunction(
                self.covfunc,
                scalar=np.asarray(other) * self.scalar,
            )

        return super().__rmul__(other)


@linfuncops.LinearFunctionOperator.__call__.register  # pylint: disable=no-member
def _(
    self, k: JaxScaledCovarianceFunction, /, *, argnum: int = 0
) -> JaxScaledCovarianceFunction:
    return k.scalar * self(k.covfunc, argnum=argnum)


class JaxSumCovarianceFunction(JaxCovarianceFunctionMixin, SumCovarianceFunction):
    def __init__(self, *summands: JaxCovarianceFunction):
        if not all(
            isinstance(summand, JaxCovarianceFunctionMixin) for summand in summands
        ):
            raise TypeError()

        super().__init__(*summands)

    @property
    def summands(self) -> tuple[JaxCovarianceFunction, ...]:
        return self._summands

    def _evaluate_jax(self, x0: jnp.ndarray, x1: Optional[jnp.ndarray]) -> jnp.ndarray:
        return functools.reduce(
            operator.add,
            (summand.jax(x0, x1) for summand in self.summands),
        )


@linfuncops.LinearFunctionOperator.__call__.register  # pylint: disable=no-member
def _(
    self, k: JaxSumCovarianceFunction, /, *, argnum: int = 0
) -> JaxSumCovarianceFunction:
    return JaxSumCovarianceFunction(
        *(self(summand, argnum=argnum) for summand in k.summands)
    )
