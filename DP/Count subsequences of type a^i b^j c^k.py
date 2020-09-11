def solve():
    ac=0
    bc=0
    cc=0
    for i in range(len(s)):
        if(s[i]=='a'):
            ac=2*ac+1
        elif(s[i]=='b'):
            bc=ac+bc*2
        else:
            cc=bc+cc*2
    print(cc)

t=int(input())
while(t>0):
    t=t-1
    s=input()
    solve()
