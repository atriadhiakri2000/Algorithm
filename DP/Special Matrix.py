def printt(table):
    for i in table:
        print(*i)

def fill(table,x,y):
    n=len(table)
    m=len(table[0])
    if(0<=x<n and 0<=y<m):
        for i in range(x,n):
            table[i][y]=-1
    return table
            
def solve(n,m,k,l):
    table=[[0 for j in range(m)] for i in range(n)] #Make the table
    printt(table)
    print()
    for i in l:
        x=i[0]
        y=i[1]
        if(0<=x<n and 0<=y<m):
            table[x][y]=-1
        else:
            print(0)
            return
        printt(table)
    printt(table)
    print()
    for i in range(m):
        if table[0][i]==0:
            table[0][i]=1
    for i in range(n):
        if table[i][0]==0:
            table[i][0]=1
    printt(table)
    print()
    for i in range(1,n):
        for j in range(1,m):
            if table[i][j]==-1:
                continue
            if table[i-1][j]>0:
                table[i][j]=table[i][j]+table[i-1][j]
            elif table[i][j-1]>0:
                table[i][j]=table[i][j]+table[i][j-1]
    printt(table)
    if (table[n - 1][m - 1] > 0): 
        print(table[n - 1][m - 1])  
    else: 
        print(0)



t=int(input())
while(t>0):
    t=t-1
    n,m,k=map(int,input().split())
    l=list(map(int,input().rstrip().rsplit()))
    x = [tuple(l[i:i + 2]) for i in range(0, len(l), 2)]
    solve(n,m,k,x)
