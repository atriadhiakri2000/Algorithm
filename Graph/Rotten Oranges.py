#code
def printt(table):
    for i in table:
        print(*i)

def adj(table,n,m,x):
    i=x[0]
    j=x[1]
    l=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    lt=[]
    for k in l:
        if(0<=k[0]<n and 0<=k[1]<m):
            if(table[k[0]][k[1]]==1):
                lt.append(k)
    return lt
    
def dfs(table,q,frs,n,m):
    y=len(q)
    visited=[]
    c=0
    while(q):
        c=c+1
        l=[]
        for j in q:
            visited.append(q)
            for i in adj(table,n,m,j):
                table[i[0]][i[1]]=2
                l.append(i)
        q=l
    if(len(visited)==y+frs):
        print(c-1)
    else:
        print(-1)

t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    l=list(map(int,input().rstrip().rsplit()))
    table=[l[i:i+m] for i in range(0,len(l),m)]
    q=[]
    frs=0
    for i in range(n):
        for j in range(m):
            if(table[i][j]==2):
                q.append((i,j))
            elif(table[i][j]==1):
                frs+=1
    dfs(table,q,frs,n,m)
