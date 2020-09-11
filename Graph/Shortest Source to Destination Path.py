def dfs(graph, node, visited, d):
    visited[node] = d
    for ng in graph.get(node, []):
        if visited.get(ng, float('inf')) > (d+1):
            dfs(graph, ng, visited, d+1)

T = int(input())
for _ in range(T):
    n, m = [int(x) for x in input().strip().split(' ')]
    arr = [int(x) for x in input().strip().split(' ')]
    r, c = [int(x) for x in input().strip().split(' ')]
    
    if arr[0] == 0:
        print(-1)
        continue
    
    mat = []
    for i in range(n):
        mat.append(arr[(i*m):((i+1)*m)])
    
    graph = dict()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                node = i*m + j
                temp = []
                
                if(i-1) >= 0:
                    if mat[i-1][j] == 1:
                        temp.append((i-1)*m + j)
                
                if (i+1) < n:
                    if mat[i+1][j] == 1:
                        temp.append((i+1)*m + j)
                
                if (j-1) >= 0:
                    if mat[i][j-1] == 1:
                        temp.append(i*m + j - 1)
                
                if (j+1) < m:
                    if mat[i][j+1] == 1:
                        temp.append(i*m + j + 1)
                
                
                graph[node] = temp
    
    # print(graph)
    
    visited = dict()
    dfs(graph, 0, visited, 0)
    dest = r*m + c
    if dest not in visited:
        print(-1)
    else:
        print(visited[dest])
                    
                    
                    
                    
                    
                    
                    
    
        
