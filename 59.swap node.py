class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def swap(node,d,k):

    if node==None:
        return

    if d%k==0:
        node.left,node.right=node.right,node.left
    swap(node.left,d+1,k)
    swap(node.right,d+1,k)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(8)
root.right.left = Node(7)
inorder(root)
print()
swap(root,0,2)
inorder(root)
print()
swap(root,0,1)
inorder(root)

