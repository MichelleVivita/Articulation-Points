from collections import defaultdict 
import matplotlib.pyplot as plt
import numpy as np
#This class represents an undirected graph  
#using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.Time = 0
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
   
    '''A recursive function that find articulation points  
    using DFS traversal 
    u --> The vertex to be visited next 
    visited[] --> keeps tract of visited vertices 
    disc[] --> Stores discovery times of visited vertices 
    parent[] --> Stores parent vertices in DFS tree 
    ap[] --> Store articulation points'''
    def APUtil(self,u, visited, ap, parent, low, disc): 
  
        #Count of children in current node  
        children =0
  
        # Mark the current node as visited and print it 
        visited[u]= True
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
  
        #Recur for all the vertices adjacent to this vertex 
        for v in self.graph[u]: 
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                low[u] = min(low[u], low[v]) 
  
                # u is an articulation point in following cases 
                # (1) u is root of DFS tree and has two or more chilren. 
                if parent[u] == -1 and children > 1: 
                    ap[u] = True
  
                #(2) If u is not root and low value of one of its child is more 
                # than discovery value of u. 
                if parent[u] != -1 and low[v] >= disc[u]: 
                    ap[u] = True    
                      
                # Update low value of u for parent function calls     
            elif v != parent[u]:  
                low[u] = min(low[u], disc[v]) 
  
  
    #The function to do DFS traversal. It uses recursive APUtil() 
    def AP(self): 
        global z
        z=[]
        # Mark all the vertices as not visited  
        # and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
        ap = [False] * (self.V) #To store articulation points 
  
        # Call the recursive helper function 
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if visited[i] == False: 
                self.APUtil(i, visited, ap, parent, low, disc) 
  
        for index, value in enumerate (ap): 
            if value == True:
                print (index)
                z.append(index)

    def drawGraph(self):
        G = nx.from_dict_of_lists(self.graph)
        color_map = []
        for u in G:
            if  u in z:
                color_map.append('red')
            else:
                color_map.append('orange')
        nx.draw(G, with_labels=True, node_color=color_map, node_size=1500, edge_color='black',linewidths=3, font_size=15)
        plt.show()

                  
import pandas
import networkx as nx
data = pandas.read_csv("edge.csv", header=0)
col_a = list(data.H1)
col_b = list(data.H2)

# Create a graph given in the above diagram 
n=int(input("Number of Vertices : "))
g=Graph(n)
for i in range(len(col_a)):
    x=col_a[i]
    y=col_b[i]
    g.addEdge(x,y)
    
print ("\nArticulation points in graph ")
g.AP()
print(z)
g.drawGraph()
