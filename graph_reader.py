from Validators_ import graph_validator


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
