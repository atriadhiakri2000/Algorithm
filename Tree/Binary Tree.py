class Node:
    def __init__(self,key):
        self.left=None
        self.right= None
        self.val=key

def insert(root,key):
    if(root is None):
        root=key
    else:
        if(root.val<key.val):
            if(root.right is None):
                root.right=key
            else:
                insert(root.right,key)
        else:
            if(root.left is None):
                root.left=key
            else:
                insert(root.left,key)

def inorder(root):
    if(root):
        inorder(root.left)
        print(root.val,sep=" ")
        inorder(root.right)

def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.val,sep=" ")

def preorder(root):
    if(root):
        print(root.val,sep=" ")
        preorder(root.left)
        preorder(root.right)

def printlevelorder(root):
    h=height(root)
    for i in range(1,h+1):
        printgivenlevel(root,i)

def printgivenlevel(root,level):
    if(root is None):
        return
    if(level==1):
        print(root.val,end=" ")
    elif(level>1):
        printgivenlevel(root.left,level-1)
        printgivenlevel(root.right,level-1)

def height(key):
    if(key is None):
        return 0
    else:
        lheight=height(key.left)
        rheight=height(key.right)

    if(lheight>rheight):
        return lheight+1
    else:
        return rheight+1

def size(root):
    if(root is None):
        return 0
    else:
        return(size(root.left)+1+size(root.right))

root=Node(9)
insert(root,Node(5))
insert(root,Node(2))
insert(root,Node(4))
insert(root,Node(11))
inorder(root)
print()
postorder(root)
print()
preorder(root)
print()
printlevelorder(root) 
print()
print(size(root))
