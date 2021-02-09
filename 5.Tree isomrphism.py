class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def isomorphism(node1,node2):
    if node1==None and node2==None:
        return True

    if node1==None or node2==None:
        return False

    if node1.val!=node2.val:
        return False

    return (isomorphism(node1.left,node2.left) and (isomorphism(node1.right,node2.right))) or (isomorphism(node1.left,node2.right) and (isomorphism(node1.right,node2.left)))


n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)

n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right = Node(7)
print(isomorphism(n1,n2))