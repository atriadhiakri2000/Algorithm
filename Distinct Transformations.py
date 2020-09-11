#Time Complexity: O(n^2)


def DT(s1,s2):
    n=len(s1)
    m=len(s2)
    if(m==0):
        return(1)
    table=[[0] * (n) for i in range(m)]
    for i in range(m):
        for j in range(i,n):
            #fill the first row
            if(i==0):
                if(j==0):
                    if(s1[j]==s2[i]):#if the first elements are same
                        table[i][j]=1
                    else:
                        table[i][j]=0#if the first elements are not same
                elif(s1[j]==s2[i]):
                    table[i][j]=table[i][j-1]+1#if the first element of s1 if same as the jth element of s2
                else:
                    table[i][j]=table[i][j-1]
            else:
                if(s1[j]==s2[i]):
                    table[i][j]=(table[i][j-1]+table[i-1][j-1])
                else:
                    table[i][j]=table[i][j-1]
    return(table[m-1][n-1])

                    
t=int(input())
while(t>0):
    t=t-1
    s1=input()
    s2=input()
    print(DT(s1,s2))
'''
2
abcccdf
abccdf
uwnny
uwnny
'''
