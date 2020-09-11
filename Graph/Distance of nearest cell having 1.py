#code
def valid(i,j,n,m,visited):
    l=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
    ans=[]
    for e in l:
        
        if(0<=e[0]<n and 0<=e[1]<m):
            if(visited[e[0]][e[1]]==-1):
                ans.append(e)
    return ans

def solve(n,m,l):
    visited=[[-1 for i in range(m)] for j in range(n)]
    q=[]
    for i in range(n):
        for j in range(m):
            if(l[i][j]==1):
                q.append((i,j))
                visited[i][j]=0
    while(q):
        p=q.pop(0)
        i=p[0]
        j=p[1]
        for e in valid(i,j,n,m,visited):
            q.append(e)
            if(l[e[0]][e[1]]==0):
                visited[e[0]][e[1]]=visited[i][j]+1
            else:
                visited[e[0]][e[1]]=0
    for i in visited:
        print(*i,end=' ')
    print()
            
t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    l=list(map(int,input().rstrip().rsplit()))
    l=[l[i:i+m] for i in range(0,n*m,m)]
    
    solve(n,m,l)
