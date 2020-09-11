from collections import defaultdict
def dfs(t,visited,i,v):
    if(visited[i]==True):
        return
    visited[i]=True
    for j in t[i]:
        dfs(t,visited,j,v)
def transpose(adj,v):
    dic=defaultdict(list)
    for i in range(v):
        for j in adj[i]:
            dic[j].append(i)
    return dic
def fill(adj,visited,stack,v):
    if(visited[v]==True):
        return
    visited[v]=True
    for i in adj[v]:
        if(visited[i]==False):
            fill(adj,visited,stack,i)
    stack.append(v)
def countSCCs (adj, v):
    stack=[]
    visited=[False]*v
    for i in range(v):
        if(visited[i]==False):
            fill(adj,visited,stack,i)
    
    t=transpose(adj,v)
    visited=[False]*v
    c=0
    while(stack):
        i=stack.pop()
        if(visited[i]==False):
            dfs(t,visited,i,v)
            c=c+1
    
    return c





#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print (countSCCs(graph, n))
        
# Contributed By: Pranay Bansal
# } Driver Code Ends
