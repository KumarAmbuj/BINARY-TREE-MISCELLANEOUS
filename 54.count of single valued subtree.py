class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findsinglevalued(node,count):
    if node==None:
        return True

    ls=findsinglevalued(node.left,count)
    rs=findsinglevalued(node.right,count)

    if ls==False or rs==False:
        return False

    if node.left and node.left.val!=node.val:
        return False
    if node.right and node.right.val!=node.val:
        return False

    count[0]+=1
    return True

def singlevalued(node):
    count=[0]
    findsinglevalued(node,count)
    print(count[0])

root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)
singlevalued(root)