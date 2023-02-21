from collections import namedtuple
from typing import Optional
from Validators_ import graph_validator

WeightedGraph = namedtuple('WeightedGraph', 'graph costs parents')


@graph_validator.validate_graph
def graph_reader(**kwargs: list[str]) -> dict[str, list[str]]:
    """
    Create a dictionary based on given keyword arguments.
    First parameter is auto assumed  as 'start'. So the first node that you send into function defined
    by the function as start.
    :param kwargs: list[str]
    :return:dict[str, list[str]]
    """
    dependency_graph = kwargs
    return dependency_graph


@graph_validator.weighted_graph_validator(is_weight_important=True)
def weighted_graph_reader(*all_vertexes: str, **weights: int) -> WeightedGraph:
    """

    :param all_vertexes: str
    :param weights: int
    :return: WeightedGraph
    """
    vertexes: dict[str, dict] = {element: dict() for element in all_vertexes}
    costs = {vertex: float('inf') if vertex != 'start' else 0 for vertex in vertexes}
    parents: dict[str, Optional[str]] = {vertex: None for vertex in vertexes if vertex != 'start'}
    for vertex, weight in weights.items():
        start_point, end_point = vertex.split('_')
        vertexes[start_point][end_point] = weight
    for key, value in vertexes['start'].items():
        costs[key] = value
        parents[key] = 'start'
    return WeightedGraph(vertexes, costs, parents)
