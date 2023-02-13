import functools
from decimal import Decimal
from pydoc import locate
from typing import Callable, ParamSpec, TypeVar, get_args

T = TypeVar('T')
P = ParamSpec('P')
Numbers = int | float | Decimal | complex


def validate_array_of_integers(parameter: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """

    :return:
    """
    parameter_type = locate(parameter)

    def inner(func: Callable[P, T]) -> Callable[P, T]:
        """

        :param func:
        :return:
        """

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            if not type(*args) == parameter_type:
                raise TypeError
            if any(map(lambda value: not isinstance(value, get_args(Numbers)), *args)):
                raise TypeError

            func_result = func(*args, **kwargs)
            return func_result

        return wrapper

    return inner
