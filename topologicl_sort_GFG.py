#Question url : https://www.geeksforgeeks.org/problems/topological-sort/1

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        in_degree = [0] * V
        queue = []
        topo = []
        # find out all in-degrees.
        for i in range(V):
            for j in adj[i]:
                in_degree[j] += 1
                
                
        # put all 0 indgree
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
                
                
        while queue:
            vertex = queue.pop(0)
            topo.append(vertex)
            for j in adj[vertex]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
        return topo
