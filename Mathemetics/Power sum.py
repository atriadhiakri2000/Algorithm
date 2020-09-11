def cal(x,n,num):
    val = (x - pow(num, n))
    if (val == 0):
        return 1
    if (val < 0):
        return 0
    return cal(val, n, num + 1) +cal(x, n, num + 1) 


 
def solve(x,n):
    return cal(x, n, 1) 

	
 
t=int(input())
while(t>0):
    t=t-1
    x=int(input())
    n=int(input())
    print(solve(x, n)) 
