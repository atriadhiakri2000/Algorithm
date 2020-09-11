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

def minValueNode( node): 
    current = node 
  
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
  
    return current  

def search(root,key):
    if(root is None or root.val==key):
        return root
    if(root.key<key):
        return(root.right,key)
    return(root.left,key)

def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.key = temp.key 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.key) 
  
  
    return root  


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
