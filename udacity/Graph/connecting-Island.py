'''
A. Problem Statements¶
In an ocean, there are n islands some of which are connected via bridges. Travelling over a bridge has some cost attaced with it.
Find bridges in such a way that all islands are connected with minimum cost of travelling.

You can assume that there is at least one possible way in which all islands are connected with each other.

You will be provided with two input parameters:

num_islands = number of islands

bridge_config = list of lists. Each inner list will have 3 elements:

 a. island A
 b. island B
 c. cost of bridge connecting both islands
Each island is represented using a number

Example:

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
'''

import heapq


def create_graphs(num_islands, bridge_config):
    graph = [ [] for _ in range(num_islands + 1)]

    for config in bridge_config:
        island = config[0]
        neighbor = config[1]
        cost = config[2]
        graph[island].append((neighbor, cost))
        graph[neighbor].append((island, cost))

    return graph

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    # Step 1 - Create a Graph
    '''
    Create a graph with given number of islands, and the cost between each pair of islands. A graph can be represented as a adjacency_matrix, which is a list of lists. For example, given:
        num_islands = 4
        bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
        
        The graph would look like:
        graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
        where, a sublist at  𝑖𝑡ℎ  index represents the adjacency_list of  𝑖𝑡ℎ  island. A tuple within a sublist is (neighbor, edge_cost).
    '''

    graph = create_graphs(num_islands, bridge_config)

    # initialize an empty list
    minHeap = list()

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # Heap is represented as a list of tuples
    # A "node" in heap is represented as tuple (edge_cost, neighbor)

    minHeap = [(0, start_vertex)]
    total_cost = 0

    while len(minHeap) > 0:
        # Here, heapq.heappop() will automatically pop out the "node" having smallest edge_cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(minHeap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost





print(get_minimum_cost_of_connecting(4, [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]))

