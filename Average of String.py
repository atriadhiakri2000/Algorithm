t=int(input())
while(t>0):
    t=t-1
    s=input()
    l=[]
    n=len(s)
    c=0
    for i in s:
        c=c+ord(i)
    print(c//n)
