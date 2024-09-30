import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    """Defines a structure of connected nodes (undirected) with an adjacency list."""
    def __init__(self):
        self.graph = {}
        
    def add_node(self, value):
        """Adds new node to the graph and returns Node object"""
        self.graph[value] = [] # neighbouring nodes represented in list
    
    def is_node(self, node):
        """Checks if node is in graph, returns True if it is, False if not."""
        return node in self.graph.keys()
    
    def add_edge(self, start_node, end_node, weight):
        """Adds edge between start_node and end_node. If either node does not exist the node is created."""
        
        # check for existance of nodes, and add as necessary
        if not self.is_node(start_node):
            self.add_node(start_node)    
        if not self.is_node(end_node):
            self.add_node(end_node)
        
        # graph is undirected, so for both nodes, add neighbouring node and weight of edge
        self.graph[start_node].append((end_node, weight)) 
        self.graph[end_node].append((start_node, weight))
    
    def draw(self):
        """Draws graph using matplotlib."""
        
        # Build graph using networkx
        G = nx.Graph() # created empty graph
        
        for node in self.graph: 
            G.add_node(node)
        
        for node, edges in self.graph.items():
            for neighbour, weight in edges:
                G.add_edge(node, neighbour, weight=weight)
        
        return G
                

class GraphApp:
    """Tkinter application to display the graph"""
    
    def __init__(self, master):
        self.master = master
        self.graph_frame = Frame(master)
        self.graph_frame.pack()
        self.draw()
    
    def draw(self):
        myGraph = Graph()
        myGraph.add_edge('A', 'B', 10)
        myGraph.add_edge('C', 'B', 20)
        myGraph.add_edge('D', 'A', 5)
        myGraph.add_edge('A', 'E', 10)
        myGraph.add_edge('C', 'D', 10)
        G = myGraph.draw()
        
        fig, ax = plt.subplots(figsize=(5, 4))  # Set the size of the figure
        pos = nx.spring_layout(G)
        weights = nx.get_edge_attributes(G, 'weight')
        
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=200, font_size=10, font_weight='bold', edge_color='gray', ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, ax=ax)
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()