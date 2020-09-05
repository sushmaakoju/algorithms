from collections import defaultdict
class Graph:
    def __init__(self):
        #use dictionary for adjacency list
        self.graph = defaultdict(list)
    
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
