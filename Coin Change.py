#https://www.youtube.com/watch?v=_fgjrs570YE

def changes(n,l,x):
    table=[0 for i in range(x+1)]
    table[0]=1
    for i in range(n):
        for j in range(l[i],x+1):
            table[j]+=table[j-l[i]]
    return(table[x])
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    coins=list(map(int,input().rstrip().rsplit()))
    change=int(input())
    print(changes(n,coins,change))
