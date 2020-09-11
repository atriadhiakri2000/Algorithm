def findSmallest(n): 
    # Case 1 - If the number is smaller than 10 
    if n < 10: 
        print (n)
        return
      
    # Case 2 - Start with 9 and try every possible digit 
    res = [] # to sort digits 
    for i in range(9,1,-1): 
        # If current digit divides n, then store all 
        # occurrences of current digit in res 
        while n % i == 0: 
            n = n / i 
            res.append(i) 
      
    # If n could not be broken in the form of digits 
    # prime factors of  n are greater than 9 
      
    if n > 10: 
        print (-1)
        return
          
    # Print the number from result array in reverse order 
    n = res[len(res)-1] 
    for i in range(len(res)-2,-1,-1): 
        n = 10 * n + res[i] 
    print (n) 

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    findSmallest(n)
