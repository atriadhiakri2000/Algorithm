#Your task is to complete this Function \
#function should return True/False
def isInterleave(a, b, c):
    # Code here
    n=len(a)
    m=len(b)
    if(n+m!=len(c)): #If the size of the final string is not same as the size of the sum of the given strings
        return False
    table=[[ False for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 and j==0): 
                table[i][j]=True
            elif(i and j and a[i-1]==c[i+j-1] and b[j-1]==c[i+j-1]):
                table[i][j]=table[i-1][j] or table[i][j-1] #If whats in a[i-1] and b[j-1] is same as c[i-1+j]
            elif(a[i-1]==c[i+j-1]): #If string a is still there
                table[i][j]=table[i-1][j]
            elif(b[j-1]==c[i+j-1]): #if string b is still there
                table[i][j]=table[i][j-1]
    return table[n][m]





    




#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends
