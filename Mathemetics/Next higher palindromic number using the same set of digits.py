from itertools import permutations

def toString(List): 
    return ''.join(List)

def solve(s):
    
    n=[]
    for i in range(len(s)):
        n.append(s[i])
    x=len(n)
    l=[]
    y=(n[0:x//2])
    print(toString(y))
    perm=permutations(y)
    for i in list(perm):
        print(i)
        i=list(i)
        l.append(toString(i))
    
    y=int(toString(y))
    ans=[]
    for i in l:
        if(int(i)>y):
            ans.append(i)

    print(ans)
    

    if(len(s)%2==1):
        o=s[len(s)//2]
        final=[]
        ans2=ans
        ans2.reverse()
        print(toString(ans),o,toString(ans2),sep="")
    else:
        ans2=ans
        ans2.reverse()
        print(toString(ans),toString(ans2),sep="")

t=int(input())
while(t>0):
    t=t-1
    s=input()
    solve(s)
