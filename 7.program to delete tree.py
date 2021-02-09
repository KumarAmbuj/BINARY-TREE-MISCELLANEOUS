class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def deletetree(node):
    if node==None:
        return None

    if node.left==None and node.right==None:
        print('deleting node',node.val)
        return None

    deletetree(node.left)
    deletetree(node.right)

    print('deleting node',node.val)
    return None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
x=deletetree(root)

