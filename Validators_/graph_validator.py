from typing import Callable, TypeVar, ParamSpec
import sys
import os
import functools

sys.path.append(os.path.join(sys.path[0], '..'))
from Exceptions_.exceptions_graph import IncorrectStartingNodeName, WrongNeighborsType, WrongInnerType


T = TypeVar('T')
P = ParamSpec('P')


def validate_graph(func: Callable[P, T]) -> Callable[P, T]:
    """
    This validator check parameters of the given func.
    1) Checking first element naming
    2) Checking types of elements
    3) If everything is ok, run the function
    :param func: Callable[P, T]
    :return: T
    """
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        if kwargs.get('start') is None:
            raise IncorrectStartingNodeName
        for value in kwargs.values():
            if not isinstance(value, list):
                raise WrongNeighborsType
            if any(map(lambda x: not isinstance(x, str), value)):
                raise WrongInnerType
        result = func(*args, **kwargs)
        return result

    return wrapper
