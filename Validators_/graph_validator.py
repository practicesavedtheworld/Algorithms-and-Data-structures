import sys
import functools
import os
from typing import Callable, TypeVar, ParamSpec

sys.path.append(os.path.join(sys.path[0], '..'))
T = TypeVar('T')
P = ParamSpec('P')


def validate_graph(func: Callable[P, T]) -> T:
    """

    :param funct:
    :return:
    """
    functools.wraps(func)

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
