from collections import deque
from graph_reader import weighted_graph_reader, WeightedGraph
from typing import Optional


def dijkstra(input_graph: WeightedGraph) -> str:
    """
    Dijkstra algorithm realization for find the shortest path based on value
    Time complexity - O(n^2 + 3*n) => O(n^2)
    Space complexity - O(2*n) => O(n)
    :return: str
    """

    result = deque(['fin'])  # O(n)
    processed = {'start': True}  # O(n)

    def find_lowest(sub_costs: dict[str, float | int]) -> Optional[str]:
        """
        Find the min cost of node in all sub_costs value
        :param sub_costs: dict[str, int | None]
        :return:str
        """

        lowest_cost_node = None
        lowest_cost = float('inf')
        # O(n)
        for node in sub_costs:
            current_cost = sub_costs[node]
            if current_cost < lowest_cost and processed.get(node) is None:
                lowest_cost = current_cost
                lowest_cost_node = node
        return lowest_cost_node

    graph, costs, parents = input_graph
    node = find_lowest(costs)
    # O(n^2)
    while node:
        new_cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors:
            if costs[neighbor] > new_cost + neighbors[neighbor]:
                costs[neighbor] = new_cost + neighbors[neighbor]
                parents[neighbor] = node
        processed[node] = True
        node = find_lowest(costs)

    # O(n)
    parent = parents['fin']
    while parents.get(parent):
        result.appendleft(parent)
        parent = parents[parent]
    result.appendleft('start')

    return ' ---> '.join(result)  # O(n)


def main():
    graph = weighted_graph_reader('start', 'a', 'b', 'c', 'fin', start_a=10, a_b=20, b_c=1, c_a=1, b_fin=30)
    print(dijkstra(graph))


if __name__ == '__main__':
    main()
