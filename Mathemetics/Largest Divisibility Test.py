def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(a, l, r):
    ans=[]
    if l==r: 
        x=int(toString(a) )
        if(x%17==0):
            ans.append(x)
            
    else: 
        for i in xrange(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack

    print(max(ans))

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    permute(str(a),0,len(a)-1)
