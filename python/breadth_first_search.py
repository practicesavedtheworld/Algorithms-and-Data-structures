from collections import deque
from typing import Optional
from graph_reader import graph_reader


def breadth_first_find(path_graph: dict[str, list[str]], looking_for: str) -> Optional[str]:
    """
    BFS algorithm realization that find the shortest path to the desired node if its exist.
    That's realization can be improved in terms of time and space.
    Time complexity is O(n + m + m + n) => O(2n + 2m) => O(n + m), n - vertexes, m - edges
    Space complexity is O(n + n + (n - 1)) => O(n)
    :param path_graph: dict[str, list[str]]
    :param looking_for: str
    :return: str | None
    """
    persons = deque(['start'])
    checked_persons: dict = {}  # mypy err - Need type annotation for "checked_persons"
    parents = {}
    while persons:
        person = persons.popleft()
        if not checked_persons.get(person):
            if person == looking_for:
                break
            else:
                neighbors = path_graph[person]
                persons.extend(neighbors)
                # finding path
                for nb in neighbors:
                    parents[nb] = person
                checked_persons[person] = True
    else:
        print("Path does not exist")
        # raise exptn
        return None
    path = deque([looking_for])
    checked_persons.clear()
    current_node = parents.get(looking_for)
    while current_node:
        if not checked_persons.get(current_node):
            checked_persons[current_node] = True
            path.appendleft(current_node)
            current_node = parents.get(current_node)
        else:
            current_node = None
    return ' --> '.join(path)


def main():
    graph = graph_reader(start=['B'], B=['K', 'F', 'C', 'D'], D=['start', 'E'], K=[], F=[], C=[])
    res = breadth_first_find(graph, 'E')
    assert res == 'start --> B --> D --> E'


if __name__ == '__main__':
    main()
