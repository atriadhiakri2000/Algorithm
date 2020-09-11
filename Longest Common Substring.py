'''def LCS(l,s):
    n1=len(l)
    n2=len(s)
    m=0
    table=[[0 for j in range(n1+1)] for i in range(n2+1)]
    for i in range(1,n2+1):
        for j in range(1,n1+1): 
            if(s[i-1]==l[j-1]):
                table[i][j]=table[i-1][j-1]+1
                if(m<table[i][j]):
                    m=table[i][j]
            else:
                table[i][j]=0
    return(m)
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    s1=input()
    s2=input()
    print(LCS(s1,s2))
'''
t=int(input())
while(t>0):
    t=t-1
    n1,n2=map(int,input().split())
    a=input()
    b=input()
    
    ans=0
    
    k = [ [0 for i in range(n1+1)] for j in range(n2+1) ]
 
    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if a[j-1]==b[i-1]:
                k[i][j]=k[i-1][j-1]+1
                if ans<k[i][j]:
                    ans=k[i][j]
            else:
                k[i][j]=0
    print (ans)
'''
t=int(input())
while(t>0):
    a=list(map(int,input().split()))
    s1=input()
    s2=input()
    maxi=0
    ans=[[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1]==s1[j-1]:
                ans[i][j]=ans[i-1][j-1]+1
                if ans[i][j]>maxi:
                    maxi=ans[i][j]
            
            
            
    print(maxi)
    t-=1
'''
