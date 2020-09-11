class BinaryTreeNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert(head):
    '''
    :param head: head of the given linked list.
    :return: root of the given binary tree
    '''
    # code here
    if not head:
        return
    
    root = BinaryTreeNode(head.data)
    stack = [root]
    temp = head.next
    
    while(temp):
        parent_node = stack[0]
        curr_node = BinaryTreeNode(temp.data)
        if not parent_node.left:
            parent_node.left = curr_node
        
        elif not parent_node.right:
            parent_node.right = curr_node
        
        if parent_node.left and parent_node.right:
            del stack[0]
        stack.append(curr_node)
        temp = temp.next
    return root
