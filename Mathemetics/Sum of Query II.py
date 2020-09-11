t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    arr=list(map(int,input().rstrip().rsplit()))
    q=int(input())
    qur1=list(map(int,input().rstrip().rsplit()))
    qur2=[qur1[i:i+2] for i in range(0,len(qur1),2)]
    ans=[]
    for i in qur2:
        x=i[0]-1
        y=i[-1]
        z=sum(arr[x:y])
        ans.append(z)
    print(*ans)
