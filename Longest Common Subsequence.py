def LCS(l,s):
    x=len(l)
    y=len(s)
    table=[[None for j in range(y+1)] for i in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if(i==0 or j==0):
                table[i][j]=0
            elif(l[i-1]==s[j-1]):
                table[i][j]=table[i-1][j-1]+1
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return(table[x][y])
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    s1=input()
    s2=input()
    print(LCS(s1,s2))
