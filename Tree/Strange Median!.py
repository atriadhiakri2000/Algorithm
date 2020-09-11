#User function Template for python3

'''

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

#User function Template for python3

def sumroot(root):
    if(root is None):
        return
    return(root.data + sumroot(root.left) + sumroot(root.right))
        
def order(root,l,k):
    if(root):
        while(len(l)!=k):
            x=root.left
            order(x,l,k)
            l.append(root.data)
            y=root.right
            order(root.right,l,k)
    return(root)
def median(root, k):
    l=[]
    r=order(root,l,k)
    s=sumroot(r)
    print(s)
    return(s//(n-k))
    
    



#{ 
#  Driver Code Starts

#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
def insert(root, node):
    if root == None:
        root = node
    else:
        if (root.data <= node.data):
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        elif (root.data > node.data):
            if (root.left == None):
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    global v
    if root:
        inorder(root.left)
        v.append(root)
        inorder(root.right)
        
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        list = [int(x) for x in input().strip().split()]
        n = list[0]
        k = list[1]
        list = [int(x) for x in input().strip().split()]
        root = Node(list[0])
        for i in range(1, n):
            insert(root, Node(list[i]))

        print(median(root, k))
        t=t-1

# } Driver Code Ends
