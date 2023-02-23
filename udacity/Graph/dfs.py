

class GraphNode():

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, newNode):
        self.children.append(newNode)

    def remove_child(self, del_node):
        self.children.remove(del_node)


class Graph():

    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


def dfs_search(root_node, search_value):


    stack = []
    visited = {root_node.value}

    stack.append(root_node)

    while len(stack) > 0:

        current_node = stack.pop()

        if current_node.value == search_value:
            return True

        for child_node in current_node.children:

            if child_node.value not in visited:
                stack.append(child_node)
                visited.add(child_node.value)

    return False


def dfs_search_recursive(node, search_value):

    visited = set()

    return dfs_search_recursive_sub(node, search_value, visited)


def dfs_search_recursive_sub(node, search_value, visited):

    visited.add(node.value)
    if node.value == search_value:
        return True

    for child_node in node.children:

        if child_node.value not in visited:

            res = dfs_search_recursive_sub(child_node, search_value, visited)
            if res:
                return True

    return False




nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# print(dfs_search(nodeS, 'S'))

print(dfs_search_recursive(nodeS, 'G'))