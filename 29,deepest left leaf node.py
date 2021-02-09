class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def finddeep(node,d,res,l):
    if node==None:
        return

    if d not in l:
        l.append(d)

        if node.left ==None and node.right==None:
            res[0]=node
    finddeep(node.left,d+1,res,l)
    finddeep(node.right,d+1,res,l)

def deepnode(node):
    res=[node]
    l=[]
    finddeep(node,0,res,l)
    print(res[0].val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.right = Node(8)

root.right.right.right.right= Node(10)
deepnode(root)
