def Kadane(l):
    n=len(l)
    currmax=l[0]
    maxsofar=l[0]
    for i in range(1,n):#maintain 2 array one for the cureent maximum value and one for the max vaue so far
        currmax=max(l[i],currmax+l[i])#comapring the max value of the currentmax plus the present element and that of the present element only
        maxsofar=max(maxsofar,currmax)
    return(maxsofar)
        
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    arr=list(map(int,input().rstrip().rsplit()))
    print(Kadane(arr))
    
