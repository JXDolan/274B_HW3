class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)] #graph[0] stores all edges connected to node 0 
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

class DisjointSet:
    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

class Solution:
    def kruskal_mst(self, graph):
        # TODO: Implement
        result = []

        i = 0 #index variable for sorted edges
        e = 0 #edges added to MST
        while e < self.V - 1:
            u, v , w = self.graph[i]
            i += 1
            x = self.find(u)
            y = self.find(v)

            if x!=y:
                e += 1
                result.append([u, v, w])
                self.union(x,y)
        
        return result


    def is_cyclic_util(self, graph, v, visited, parent):
        # TODO: Implement
        pass

    def is_cyclic(self, graph):
        # TODO: Implement
        pass

    def detect_deadlock(self, graph):
        # TODO: Implement
        pass


    #REFERENCES 
    # https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
