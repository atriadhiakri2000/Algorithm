# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges
def solve(v,i,l,a):
    v[i]=True
    for j in a[i]:
        if(v[j]==False):
            solve(v,j,l,a)
    l.append(i)

def topoSort(n, adj):
    # Code here
    visited=[False for i in range(n)]
    l=[]
    for i in range(n):
        if(visited[i]==False):
            solve(visited,i,l,adj)
    l.reverse()
    return(l)




#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        
        if check(graph, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
