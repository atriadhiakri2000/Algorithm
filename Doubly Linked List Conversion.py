t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().rstrip().rsplit()))
    l.reverse()
    print(*[l[x] for x in range(n)], sep='<-')

'''
def makeDoubly(head):
    #your code here
    if(head==None or head.next==None):
        return(head)
    cur=head
    l=[]
    while(cur!=None):
        l.append(cur.data)
        cur=cur.next
    n=len(l)
    arr=[]
    l.reverse()
    for i in range(n):
        arr.append(l[i])
        arr.append("<-")
    arr.pop()
    y=" ".join(str(x) for x in arr)
    print(y)'''
