from typing import Callable, TypeVar, ParamSpec, cast
import functools
import os
import re
import sys

sys.path.append(os.path.join(sys.path[0], '..'))
from Exceptions_.exceptions_graph import *

T = TypeVar('T')
P = ParamSpec('P')


def validate_graph(func: Callable[P, T]) -> Callable[P, T]:
    """
    This validator check parameters of the given func.
    1) Checking first element naming
    2) Checking types of elements
    3) If everything is ok, run the function
    :param func: Callable[P, T]
    :return: Callable[P, T]
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


def weighted_graph_validator(is_weight_important: bool = True) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Based on given parameter validate wrapped function
    is_weight_important can be [True, False]
    :param is_weight_important: bool
    :return: Callable[[Callable[P, T]], Callable[P, T]]
    """

    def inner_validator(func: Callable[P, T]) -> Callable[P, T]:
        """
        Checking function and if its incorrect raise exceptions
        :param func: Callable[P, T]
        :return: Callable[P, T]
        """

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            if 'start' not in args:
                raise ExcludedStart
            elif 'fin' not in args:
                raise ExcludedFinish
            if is_weight_important:
                for vertex, weight in kwargs.items():
                    weight = cast(int | float, weight)
                    if weight < 0:
                        raise NegativeWeightInGraph
                    if not re.fullmatch(r'.+_.+', vertex):
                        raise MissingNodeSeparator
            func_result = func(*args, **kwargs)
            return func_result

        return wrapper

    return inner_validator
