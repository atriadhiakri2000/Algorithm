def countWays(n):
    mod = 1000000007
    res=m//2
    res=res+1
    res=res%mod
    return (res)

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    countWays(n)
 
