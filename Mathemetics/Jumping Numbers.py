def bfs(x,num):
    q=[]
    q.append(num)
    l=[]
    while(q):
        n=q.pop(0)
        if(n<=x):
            l.append(n)
            last_digit=n%10
            if(last_digit==0):
                y=(n*10)+(last_digit+1)
                q.append(y)
            elif(last_digit==9):
                y=(n*10)+(last_digit-1)
                q.append(y)
            else:
                y=(n*10)+(last_digit-1)
                q.append(y)
                y=(n*10)+(last_digit+1)
                q.append(y)
    return(l)

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    print (0, end =' ')
    l=[]
    ans=[]
    for i in range(1,10):
        l.append(bfs(n,i))
    for i in l:
        for j in i:
            ans.append(j)
    ans.sort()
    print(*ans)
