from decimal import Decimal
from pydoc import locate
from typing import Callable, ParamSpec, TypeVar, get_args
import functools
import os
import sys

sys.path.append(os.path.join(sys.path[0], '..'))
from Exceptions_.exceptions_sorting import WrongInnerTypeOfArray

T = TypeVar('T')
P = ParamSpec('P')
Numbers = int | float | Decimal | complex


def validate_array_of_numbers(parameter: str = 'list') -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Based on given parameter validate wrapped function
    parameter can be [list, ]
    :parameter parameter: str
    :return: Callable[[Callable[P, T]], Callable[P, T]]
    """
    parameter_type = locate(parameter)

    def inner(func: Callable[P, T]) -> Callable[P, T]:
        """
        Checking what input type we received, if its incorrect raise exception
        :param func: Callable[P, T]
        :return: Callable[P, T]
        """

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            type_of_arg = type(*args)
            if type_of_arg != parameter_type:
                raise TypeError(f"Wrong type, it await {parameter}", type_of_arg)
            if any(map(lambda value: not isinstance(value, get_args(Numbers)), *args)):
                raise WrongInnerTypeOfArray(get_args(Numbers))

            func_result = func(*args, **kwargs)
            return func_result

        return wrapper

    return inner
