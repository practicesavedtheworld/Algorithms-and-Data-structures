class IncorrectStartingNodeName(Exception):
    def __str__(self):
        return f"""First argument must be named as 'start'
For example start=['1', '2', '3']"""


class ExcludedStart(Exception):
    def __str__(self):
        return "There is no 'start' node in graph or its called incorrect. Add your starting point as 'start'"


class ExcludedFinish(Exception):
    def __str__(self):
        return "There is no 'fin' node in graph or its called incorrect. Add your final point called as 'fin'"


class NegativeWeightInGraph(Exception):
    def __str__(self):
        return "That realization doesn't work with negative weights pathing. Use graph with positive weights"


class MissingNodeSeparator(Exception):
    def __str__(self):
        return """Path from point to point must be separated by the '_' symbol.
For e.g path from A to B that weights 14 handle like this  A_B=14, provided that A is not the starting vertex.
Starting vertex must be called 'start'"""


class WrongNeighborsType(Exception):
    def __str__(self):
        return f"""Neighbor nodes(element) must be in list-type
For e.g node=['node1', 'node2', 'node3']"""


class WrongInnerType(Exception):
    def __str__(self):
        return f"""Node relation nodes must be str type
For example, A=['10', '11', ..., 'n']
                /      /     /    /
              str    str   str  str"""
