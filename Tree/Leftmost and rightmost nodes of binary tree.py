from collections import deque


# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Iterative function to print corner nodes of every level in binary tree
def printTree(root):

    # return if tree is empty
    if root is None:
        return

    # create an empty queue to store Tree nodes
    q = deque()

    # enqueue root node
    q.append(root)

    # loop till queue is empty
    while q:

        # get size of current level
        size = len(q)
        n = size

        # process all nodes present in current level
        while n:
            n = n - 1
            node = q.popleft()

            # if corner node found, print it
            if n == size - 1 or n == 0:
                print(node.data, end=' ')

            # enqueue left and right child of current node
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        # terminate level by printing newline
        print()


if __name__ == '__main__':

    """ Construct below tree
                 1
                / \
               /   \
              2     3
             /     / \
            /     /   \
           4     5     6
          /     / \     \
         /     /   \     \
        7     8     9     10
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.right.left.left = Node(8)
    root.right.left.right = Node(9)
    root.right.right.right  = Node(10)

    printTree(root)
