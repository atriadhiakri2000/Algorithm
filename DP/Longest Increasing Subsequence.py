def LIS(l):
    n=len(l)
    lt=[1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if(l[i]>l[j]):
                lt[i]=max(lt[i],lt[j]+1)
    maxo=0
    for i in range(n):
        maxo=max(maxo,lt[i])
    return(maxo)
        
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    arr=list(map(int,input().rstrip().rsplit()))
    print(LIS(arr))
