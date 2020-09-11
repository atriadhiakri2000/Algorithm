#code
def TDM(s):
    n=len(s)
    table=[0]*(n+1)
    table[0]=1
    table[1]=1
    for i in range(2,n+1):
        table[i]=0
        if(s[i-1]>'0'):
            table[i]=table[i-1]
        if(s[i-2]=='1' or s[i-2]=='2' and s[i-1]<'7'):
            table[i]=table[i-2]+table[i]
    if(s[0]=='0'):
        print(0)
    else:
        print(table[n])

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input()
    TDM(s)
