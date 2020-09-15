'''
Using Dijkstra's algorithm, find the shortest path to all the nodes starting from a given single source node.
You need to print the distance of each node from the given source node.
Example:
the distance of each node from A would be printed as,
{'A': 0, 'D': 2, 'B': 5, 'E': 4, 'C': 3, 'F': 6}

1. result dictionary = { }, will be printed
2. distance from source to source itself is 0. 
3. distance to all other nodes from the source is unknown initially (set to infinity)
4. unvisited set = set(). initially all nodes are in there.
5. path dictionary = {} to keep track of the previous node (value) that can lead to the current node (key).
    ex) {'B': 'A', 'C': 'D', 'D': 'A', 'F': 'C', 'E': 'C'} B의 이전 노드는 A, C의 이전 노드는 D
6. loop (repeat) until unvisited dictionary is empty:
    1) find th smallest distance node from the source in unvisited set.
    2) for the current node, find all unvisited neighbor nodes by calculating the distance of each unvisited neighbor nodes.
    3) if the calculated distance of the unvisited neighbor node is less than the already known distance in result dictionary,
        update the shortest distance in the result dictionary.
    4) if the result dictionary is updated already, update the path dictionary as well for the same key.
    5) remove the current node from the unvisited set.
TC: O(n^2)
'''

from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()  # A set cannot contain duplicate nodes
        self.neighbors = defaultdict(list)  # defaultdict is a child class of Dictionary that provides a default value for a key that does not exist.
        self.distances = {} # dictionary. ex) ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbors[from_node].append(to_node)
        self.neighbors[to_node].append(from_node)
        self.neighbors[(from_node, to_node)] = distance
        self.neighbors[(to_node, from_node)] = distance

    def print_graph(self):
        print('Set of nodes are: ', self.nodes)
        print('Neighbors are: ', self.neighbors)
        print('Distances are: ', self.distances)

import sys
def shortest_path_dijkstra(graph, source):
    result = {}
    
    for node in graph.nodes:
        if node == source:
            result[node] = 0
        else:
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)
    path = {}

    # greedy algorithm
    while unvisited:
        # 1. find the shortest node 
        shortest_node = None
        for node in unvisited:
            if node in result:
                if shortest_node is None:
                    shortest_node = node
                elif result[node] < result[shortest_node]:
                    shortest_node = node

        if shortest_node is None:
            break

        current_distance = result[shortest_node]

        # 2. for the current node, find all the unvisited neighbor nodes by calculating the distance of each unvisited neighbor node.
        for neighbor in graph.neighbors[shortest_node]:
            if neighbor in unvisited:
                distance = current_distance + graph.distances[(shortest_node, neighbor)]

                # 3. if the calculated distance 
                if (neighbor not in result) or distance < result[neighbor]:
                    result[neighbor] = distance

                    # 4. if there is an update in the result dictionary, update the path dictionary for the same key.
                    path[neighbor] = shortest_node

        # 5. remove the current node from the unvisited set.
        unvisited.remove(shortest_node)

    return result

# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

print(testGraph.nodes)
testGraph.add_edge('A', 'B', 3)
testGraph.add_edge('A', 'D', 2)
testGraph.add_edge('B', 'D', 4)
testGraph.add_edge('B', 'E', 6)
testGraph.add_edge('B', 'C', 1)
testGraph.add_edge('C', 'E', 2)
testGraph.add_edge('E', 'D', 1)
print(testGraph.print_graph())

print(shortest_path_dijkstra(testGraph, 'A'))
