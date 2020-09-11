def most(db,m):
    return [k for k, v in db.items() if v == m]

def CF(l):
    dict={}
    for i in l:
        dict[i]=l.count(i)
    return(dict)
    
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(str,input().rstrip().rsplit()))
    l.sort()
    x=CF(l)
    lt=list(dict.fromkeys(l))
    fre=[]
    for i in lt:
        fre.append(l.count(i))
    m=max(fre)
    ko=most(x,m)
    ko.sort()
    print(ko[0])
