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
        #sort graph ref: https://learnpython.com/blog/sort-tuples-in-python/
        #sort by weights, that is the second index
        #graph.graph = sorted(graph.graph, key=lambda item:item[1]) getting 6/11 on gradescope using this

        #geeks for geeks is using a list of edges not an adjacency edge list, must convert adj list to list of edges to follow gfg format
        #make edge list ref: https://youcademy.org/conversion-between-edge-list-adjacency-list/#:~:text=To%20convert%20from%20an%20adjacency,it%20to%20the%20edge%20list.
        edge_list = []
        
        for node in range(len(graph.graph)):
            for adj_node, weight in graph.graph[node]:
                edge_list.append([node, adj_node, weight])

        edge_list_sorted = sorted(edge_list, key = lambda item: item[2])
        ds = DisjointSet(graph.V)

        i = 0 #index variable for sorted edges
        e = 0 #edge count in MST
        while e < graph.V - 1 and i < len(edge_list_sorted):
            u, v , w = edge_list_sorted[i]
            i += 1
            x = ds.find(u)
            y = ds.find(v)

            if x!=y:
                e += 1
                #result.append([u, v, w])
                result.append([u, v, w])
                ds.union(x,y)
        
        return result


    def is_cyclic_util(self, graph, v, visited, parent):
        # TODO: Implement
        visited[v] = True

        for i , weight in graph.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(graph, i, visited, v ):
                    return True
                
                #adj vertex visited and isnt parent of the current vertex then a cycle exists
            elif i != parent:
                return True
                
        return False
            
        

    def is_cyclic(self, graph):
        # TODO: Implement
        visited = [False] * len(graph.graph)

        for u in range(len(graph.graph)):
            if not visited[u]:
                if self.is_cyclic_util(graph, u, visited, -1):
                    return True
                
        return False


    def detect_deadlock(self, graph):
        # TODO: Implement
        return self.is_cyclic(graph)
           

'''
REFERENCES 
for kruskal's
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

for is_cyclic_util and is cyclic
https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
'''