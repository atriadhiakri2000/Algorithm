t=int(input())
while t>0:
    t-=1
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=list(set(l1+l2))
    l3.sort()
    l3=l3[::-1]
    l=l3[:n]
    k=0
    l4=[]
    l5=[]
    for i in l1:
        if i not in l4:
            l4.append(i)
    for i in l2:
        if i not in l5:
            l5.append(i)
    k=0
    for i in l5:
        if i in l:
            l.remove(i)
            l.insert(k,i)
            k+=1
    for i in l4:
        if i not in l2:
            if i in l:
                l.remove(i)
                l.insert(k,i)
                k+=1
    print(*l)
'''
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    arr1=list(map(int,input().rstrip().rsplit()))
    arr2=list(map(int,input().rstrip().rsplit()))
    arr1.sort()
    arr1.reverse()
    arr2.sort()
    arr2.reverse()
    arr3=arr2+['a']+arr1
    arr3=list(dict.fromkeys(arr3))
    print(*arr3)
    i=arr3.index("a")
    l1=arr3[0:i]
    l2=arr3[i+1:len(arr3)]
    print(l1,l2)
    x=n//2
    final=[]
    final2=[]
    if(n%2==0):
        if(len(l1)>=len(l2)):
            if(len(l2)<x):
                y=x-len(l2)
                final=l1[0:y]+l2
                print(*final)
            else:
                final=l1[0:x]+l2[0:x]
                print(*final)
        else:
            l1,l2=l2,l1
            if(len(l2)<x):
                y=x-len(l2)
                final=l1[0:y]+l2
                print(*final)
            else:
                final=l1[0:x]+l2[0:x]
                print(*final)
    else:
        if(len(l1)>=len(l2)):
            if(len(l2)<x):
                y=x-len(l2)
                final=l1[0:y+1]+l2
                print(*final)
            else:
                final=l1[0:x]+l2[0:x+1]
                final2=l1[0:x+1]+l2[0:x]
                if(sum(final)>sum(final2)):
                    print(*final)
                else:
                    print(*final2)
        else:
            l1,l2=l2,l1
            if(len(l2)<x):
                y=x-len(l2)
                final=l1[0:y+1]+l2
                print(*final)
            else:
                final=l1[0:x]+l2[0:x+1]
                final2=l1[0:x+1]+l2[0:x]
                if(sum(final)>sum(final2)):
                    print(*final)
                else:
                    print(*final2)
'''
