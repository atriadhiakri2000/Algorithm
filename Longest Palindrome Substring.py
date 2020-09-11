
def reverse(string): 
    string = "".join(reversed(string)) 
    return string

# you need to complete this function
def longestPalindrome(s):
    # code here
    n=len(s)
    new=[]
    for i in range(n):
        for j in range(i+1,n+1):
            if(s[i:j]==reverse(s[i:j])):
                new.append(s[i:j])
    c=[]
    for i in new:
        c.append(len(i))
    m=0
    m=c.index(max(c))
    return(new[m])



#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver program to test above functions

if __name__=='__main__':
    tc=int(input())
    for _ in range(tc):
        str=input()
        print(longestPalindrome(str))
# } Driver Code Ends
