#Time complexity: O(N^2)
#Auxiliary Space: O(N^2)
def FAP(s):
    n=len(s)
    table=[[0]*n for i in range(n)]
    x=0
    y=0
    gap=0
    for gap in range(1,n):
        x=0
        for y in range(gap,n):
            if(s[y]==s[x]):
                table[x][y]=table[x+1][y-1]#diagonal element
            else:
                table[x][y]=min(table[x][y-1],table[x+1][y])+1
            x=x+1
    return(table[0][n-1])
            
t=int(input())
while(t>0):
    t=t-1
    s=input()
    print(FAP(s))
