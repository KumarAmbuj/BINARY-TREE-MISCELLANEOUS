class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def deletenode(node,k,l):

    if node==None:
        return None

    node.left=deletenode(node.left,k,l+1)
    node.right=deletenode(node.right,k,l+1)

    if node.left==None and node.right==None:
        if l<k:
            return None

    return node
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)

k = 4
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.left.left.left = newNode(7)
root.right.right = newNode(6)
root.right.right.left = newNode(8)
inorder(root)
print()
node=deletenode(root,k,1)
inorder(node)
