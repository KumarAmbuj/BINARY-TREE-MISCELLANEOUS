class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def height(node,l):
    if node==None:
        return 0

    if node.left==None and node.right==None:
        if l%2==0:
            return 1
        else:
            return 0

    l=height(node.left,l+1)
    r=height(node.right,l+1)

    if l==0 and r==0:
        return 0
    return max(l,r)+1


root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
print("Height of tree is",height(root,1))
