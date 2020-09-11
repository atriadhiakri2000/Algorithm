def solve(n):
    table=[0]*(n+1)    
    for i in range(1,n+1):
        if(i<=3):
            table[i]=1
        elif(i==4):
            table[i]=2
        else:
            table[i]=table[i-1]+table[i-4]
    return table[n] 
    


t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    print(solve(n))
