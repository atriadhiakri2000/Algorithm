#code
def solve(l,n,s):

    table=[[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(0,n+1):
        table[i][0] = 1
    
    
    for i in range(1,n+1):
        for j in range(1,s+1):
            if(j<l[i-1]):
                table[i][j]=table[i-1][j]
            else:
                table[i][j]=table[i-1][j-l[i-1]] + table[i-1][j]
    for i in table:
        print(*i)
    print(table[n][s])
    
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().rstrip().rsplit()))
    s=int(input())
    solve(l,n,s)
   
