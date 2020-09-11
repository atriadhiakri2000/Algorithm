def pretopost(arr,n,i,min_val,max_val):

    if(i[0]==n):
        return
    if(arr[i[0]]<min_val or arr[i[0]]>max_val):
        return
    val=arr[i[0]]
    i[0]=i[0]+1
    pretopost(arr,n,i,min_val,val)
    pretopost(arr,n,i,val,max_val)
    print(val,end=" ")

def solve(arr,n):
    i=[0]
    min_val=-999999999999
    max_val=999999999999
    pretopost(arr,n,i,min_val,max_val)
    
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    arr=list(map(int,input().rstrip().rsplit()))
    solve(arr,n)
    print()
 
