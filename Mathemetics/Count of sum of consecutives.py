def solve(N): 
      
    # constraint on values of L gives us the  
    # time Complexity as O(N^0.5) 
    count = 0
    L = 1
    while( L * (L + 1) < 2 * N): 
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1) 
        if (a - int(a) == 0.0): 
            count += 1
        L += 1
    return(count)
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    print(solve(n))
