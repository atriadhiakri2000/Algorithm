def solve():
    i=0
    j=n-1
    c=0
    while(i<=j):
        if(l[i]==l[j]):
            i=i+1
            j=j-1
        elif(l[i]>l[j]):
            j=j-1
            l[j]=l[j]+l[j+1]
            c=c+1
        else:
            i=i+1
            l[i]=l[i]+l[i-1]
            c=c+1
    print(c)
    
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().rstrip().rsplit()))
    solve()
