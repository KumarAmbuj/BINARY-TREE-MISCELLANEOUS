class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def findw(node,l,d):
    if node==None:
        return

    if d not in l:
        l.append(d)

    findw(node.left,l,d-1)
    findw(node.right,l,d+1)
def findwidth(node):
    l=[]
    findw(node,l,0)
    print(len(l))

root = Node(7)
root.left = Node(6)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(1)
findwidth(root)