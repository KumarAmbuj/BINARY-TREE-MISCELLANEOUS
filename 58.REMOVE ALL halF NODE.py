class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def removehalfnode(node):
    if node==None:
        return None

    node.left=removehalfnode(node.left)
    node.right=removehalfnode(node.right)

    if node.left==None and node.right==None:
        return node

    if node.left==None:
        return node.right
    if node.right==None:
        return node.left
    return node
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
inorder(root)
print()
node=removehalfnode(root)
inorder(node)