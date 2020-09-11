class adjnode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V

    def add_edge(self,scr,dest):
        node=adjnode(dest)
        node.next=self.graph[scr]
        self.graph[scr]=node
        
        node=adjnode(scr)
        node.next=self.graph[dest]
        self.graph[dest]=node

    def display(self):
        for i in range(self.V):
            print("{} head".format(i),end="")
            temp=self.graph[i]
            while(temp):
                print(" -> {}".format(temp.data), end="")
                temp=temp.next
            print(" \n")

if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.display() 
