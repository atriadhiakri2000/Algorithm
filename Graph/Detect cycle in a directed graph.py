# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices

def solve(visited,stack,i):
    visited[i]=True
    stack[i]=True
    for j in graph[i]:
        if(visited[j]==False):
            if solve(visited,stack,j)==True: 
                return True
        elif stack[j]==True: #Since we are visiting all the nodes=d that can be visited from this node and to check if it is in the stck or not to prove ot its has been visited or not
            return True #This means the loop existed so we return true
    stack[i]=False #This means the loop didint existed so we make it back to false
    return False
            
        

def isCyclic(n, graph):
    # Code here
    visited=[False]*n
    stack=[False]*n
    for i in range(n):
        if(visited[i]==False):
            if(solve(visited,stack,i)==True:
               return True
    return False








    



#{ 
#  Driver Code Starts

from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends
