def adj(mat,c,n,m):
    x=c[0]
    y=c[1]
    l=[]
    trv=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for i in trv:
        if(0<=i[0]<n and 0<=i[1]<m):
            a=i[0]
            b=i[1]
            if(mat[a][b]=='X'):
                l.append(i)
    return l

def bsf(v,e,m,n,mat):
    q=[e]
    while(q):
        c=q.pop(0)
        al=adj(mat,c,n,m)
        for i in al:
            if(i not in v):
                v.add(i)
                q.append(i)

def solve(mat,m,n):
    visited=set()
    c=0
    for i in range(n):
        for j in range(m):
            if(mat[i][j]=='X'):
                if (i,j) not in visited:
                    visited.add((i,j))
                    c=c+1
                    bsf(visited,(i,j),m,n,mat)
    print(c)

t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    l=list(map(str,input().rstrip().rsplit()))
    mat=[]
    for i in l:
        o=[]
        for j in i:
            o.append(j)
        mat.append(o)
    solve(mat,m,n)
