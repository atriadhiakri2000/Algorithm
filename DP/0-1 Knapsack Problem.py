#NOT OPTIMIZED
'''def knapsack(total,capacity,value,n):
    if n == 0 or total == 0 : 
        return 0
    if(capacity[n-1]>total):#Since the value of the n-1th item is less than the weight hence there is no point of including the value 
        return knapsack(total,capacity,value,n-1)
    else:#find the max value by including the nth item and without including the nth item
        x=max((value[n-1]+knapsack(total-capacity[n-1],capacity,value,n-1)),knapsack(total,capacity,value,n-1))
        return (x)
'''
'''
#OPTIMIZED
def knapsack(total,capacity,value,n):
    l=[[0 for i in range(total+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(total+1):
            if(i==0 or j==0):
                l[i][j]=0
            elif(capacity[i-1]<=j):
                l[i][j]=max( (value[i-1] + l[i-1][j - capacity[i-1]]) , l[i-1][j])
            else:
                l[i][j]=l[i-1][j]
    return(l[i][total])
'''
'''
def knapsack(wt, val, W, n):     
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
  
    if wt[n-1] <= W: 
        t[n][W] = max( 
val[n-1] + knapsack( 
wt, val, W-wt[n-1], n-1),  
knapsack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = knapsack(wt, val, W, n-1) 
        return t[n][W]
'''
def knapsack(wt,val,W,n):
    l=[0]*(W+1)
    for i in range(n):
        for j in range(W,wt[i],-1):
            l[j]=max(l[j],val[i]+l[j-wt[i]])
    return l[W]

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    W=int(input())
    val=list(map(int,input().rstrip().rsplit()))
    wt=list(map(int,input().rstrip().rsplit()))
    print(knapsack(wt, val, W, n))

