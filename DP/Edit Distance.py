def ED(s1,s2):
    m=len(s1)
    n=len(s2)
    table=[ [0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0):
                table[i][j]=j
            elif(j==0):
                table[i][j]=i
            elif(s1[i-1]==s2[j-1]):
                table[i][j]=table[i-1][j-1]
            else:
                table[i][j]=1+min(table[i-1][j],table[i][j-1],table[i-1][j-1])
    print(table[m][n])
    

t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    s1,s2=map(str,input().split())
    ED(s1,s2)
