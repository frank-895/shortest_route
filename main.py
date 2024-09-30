# create graph structure

class Node:
    """Defines a single node in the graph."""
    def __init__(self, value):
        self.value = value

class Graph:
    """Defines a structure of connected nodes (undirected) with an adjacency list."""
    def __init__(self):
        self.graph = {}
        
    def add_node(self, value):
        """Adds new node to the graph and returns Node object"""
        new_node = Node(value)
        self.graph[new_node] = [] # neighbouring nodes represented in list
    
    def is_node(self, node):
        """Checks if node is in graph, returns True if it is, False if not."""
        return node in self.graph.keys()
    
    def add_edge(self, start_node, end_node, weight):
        """Adds edge between start_node and end_node. If either node does not exist the node is created."""
        
        # check for existance of nodes, and add as necessary
        if not start_node.is_node():
            self.add_node(start_node)    
        if not end_node.is_node():
            self.add_node(end_node)
        
        # graph is undirected, so for both nodes, add neighbouring node and weight of edge
        self.graph[start_node].append((end_node, weight)) 
        self.graph[end_node].append((start_node, weight))