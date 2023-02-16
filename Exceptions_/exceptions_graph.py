class IncorrectStartingNodeName(Exception):
    def __str__(self):
        return f"""First argument must be named as 'start'
For example start=['1', '2', '3']"""


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
