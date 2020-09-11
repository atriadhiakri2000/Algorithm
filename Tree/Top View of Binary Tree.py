#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def solve(dic,dist,lvl,root):
    if root is None:
        return
    if(dist not in dic or lvl<dic[dist][1]):
        dic[dist]=(root.data,lvl)
    solve(dic,dist-1,lvl+1,root.left)
    solve(dic,dist+1,lvl+1,root.right)
    
    
def topView(root):
    dic={}
    solve(dic,0,0,root)
    for i in sorted(dic.keys()):
        print(dic.get(i)[0],end=" ")
    print()







#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Contributed by Sudarshan Sharma

from collections import deque
import queue 

class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()

# } Driver Code Ends
