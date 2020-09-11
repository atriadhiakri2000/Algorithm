#code
def countWays(n):
    mod=1000000007
    fibo=[]
    fibo.append(0)
    fibo.append(1)
    fibo.append(2)
    fibo.append(3)
    for i in range(4,100000+1):
        fibo.append((fibo[i-1]%1000000007+fibo[i-2]%1000000007)%1000000007)
    print(fibo[-1])

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    countWays(n)
 
 
