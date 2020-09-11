def Tree(p,s,n,post,dic):
    if(s>n):
        return None,p
    root=Node(post[p])
    p=p-1
    i=dic[root.data]
    root.right,p=Tree(p,i+1,n,post,dic)
    root.left,p=Tree(p,s,i-1,post,dic)
    return root,p

def buildTree(In, post, n):
    dic={}
    for i,e in enumerate(In):
        dic[e]=i
    p=n-1
    return Tree(p,0,n-1,post,dic)[0]
