#code
def MNJ(l):
    n=len(l)
    if(n<=1):
        return (0)
    if(l[0]==0):
        return (-1)
    jump=1
    x=l[0]#Has the first value coz thats the max we can jump
    steps=l[0]#Has the total number of steps left to make 
    for i in range(1,n):
        if(i==n-1):
            return jump
        x=max(x,i+l[i])#Compare the all ready made steps with the new number of steps to be made
        steps=steps-1#One step is completed to remove it
        if(steps==0):
            jump=jump+1#Since the number of steps are equal to zero so we can claim that the number of steps lef for him to do is equal to 0 so he needs to make one jump
            if(i>=x):
                return (-1)#The jump can be made only if the number of max steps is more the then i
            steps=x-i#New number of steps that we can do
    return (-1)
    
    
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().rstrip().rsplit()))
    print(MNJ(l))
