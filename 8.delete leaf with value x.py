class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


def deleteleaf(node,x):
    if node==None:
        return None

    
    node.left=deleteleaf(node.left,x)
    node.right=deleteleaf(node.right,x)
    if node.val==x and node.left==None and node.right==None:
        return None

    return node

root = Node(10)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(3)
root.left.right = Node(1)
root.right.right = Node(3)
root.right.right.left = Node(3)
root.right.right.right = Node(3)
inorder(root)
node=deleteleaf(root, 3)
print()
inorder(node)



