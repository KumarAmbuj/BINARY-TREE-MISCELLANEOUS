class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def height(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 0

    l=height(node.left)
    r=height(node.right)

    return max(l,r)+1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(height(root))