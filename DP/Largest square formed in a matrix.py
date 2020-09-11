def solve(n,m,mat):
    table=[[0 for i in range(m+1)] for j in range(n+1)]
    maxe=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(mat[i-1][j-1]==0):
                table[i][j]=0
            else:
                table[i][j]=min(table[i][j-1],table[i-1][j],table[i-1][j-1])+1
                maxe=max(maxe,table[i][j])
    
    print(maxe)

t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    l=list(map(int,input().rstrip().rsplit()))
    mat=[l[i:i+m] for i in range(0,n*m,m)]
    solve(n,m,mat)
