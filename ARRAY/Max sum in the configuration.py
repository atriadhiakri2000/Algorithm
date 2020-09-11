#User function Template for python3

def max_sum(a,n):
    #code here
    m=0
    c=0
    while(c<n):
        c=c+1
        s=0
        for i in range(n):
            s=s+(i*a[i])
        m=max(m,s)
        a=a[-1:]+a[:-1]
    return(m)

or

def max_sum(a,n):
    cum_sum=0
    for i in range(0,n):
        cum_sum=cum_sum+a[i]
    initial_value=0
    mx=0
    for i in range(0,n):
        initial_value+=i*a[i]
        mx=initial_value
    for i in range(1,n):
        temp=initial_value-(cum_sum-a[i-1])+a[i-1]*(n-1)
        initial_value=temp
        if(temp>mx):
            mx=temp
    return mx


#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends
