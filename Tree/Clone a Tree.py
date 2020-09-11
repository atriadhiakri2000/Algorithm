
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
# Data structure to store the special binary tree node with random pointer
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None, random=None):
        self.data = data
        self.left = left
        self.right = right
        self.random = random
 
 
# Function to print the preorder traversal of a binary tree
def preorder(root):
 
    if root is None:
        return
 
    # print data
    print(root.data, end=" -> ( ")
 
    # print left child's data
    print((root.left.data if root.left else "X"), end=", ")
 
    # print right child's data
    print((root.right.data if root.right else "X"), end=", ")
 
    # print random child's data
    print((root.random.data if root.random else "X"), ")")
 
    # recur for the left and right subtree
    preorder(root.left)
    preorder(root.right)
 
 
# Recursive function to copy random pointers from the original binary tree
# into the cloned binary tree using the dict
def updateRandomPointers(root, dict):
 
    # base case
    if dict.get(root) is None:
        return
 
    # update the random pointer of cloned node
    dict.get(root).random = dict.get(root.random)
 
    # recur for left and right subtree
    updateRandomPointers(root.left, dict)
    updateRandomPointers(root.right, dict)
 
 
# Recursive function to clone the data, left and right pointers for
# each node of a binary tree into a given dict
def cloneLeftRightPointers(root, dict):
 
    # base case
    if root is None:
        return None
 
    # clone all fields of the root node except the random pointer
 
    # create a node with same data as root node
    dict[root] = Node(root.data)
 
    # clone the left and right subtree
    dict[root].left = cloneLeftRightPointers(root.left, dict)
    dict[root].right = cloneLeftRightPointers(root.right, dict)
 
    # return cloned root node
    return dict[root]
 
 
# Main function to clone a special binary tree with random pointers
def cloneSpecialBinaryTree(root):
 
    # create a dictionary to store mappings from a node to its clone
    dict = {}
 
    # clone data, left and right pointers for each node of the original
    # binary tree and put references into the dict
    cloneLeftRightPointers(root, dict)
 
    # update random pointers from the original binary tree into the dict
    updateRandomPointers(root, dict)
 
    # return the cloned root node
    return dict[root]
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    root.random = root.right.left.random
    root.left.left.random = root.right
    root.left.right.random = root
    root.right.left.random = root.left.left
    root.random = root.left
 
    print("Preorder traversal of the original tree:")
    preorder(root)
 
    clone = cloneSpecialBinaryTree(root)
 
    print("\nPreorder traversal of the cloned tree:")
    preorder(clone)
 
T
Tr
