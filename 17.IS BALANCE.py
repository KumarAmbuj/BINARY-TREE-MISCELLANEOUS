class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Pair():
    def __init__(self,flag=False,h=0):
        self.flag=flag
        self.h=h
def isBalance(node):

    if node==None:
        np=Pair(True,0)
        return np

    lp=isBalance(node.left)
    rp=isBalance(node.right)

    np=Pair()

    np.flag=(abs(lp.h-rp.h)<=1)and lp.flag and rp.flag
    np.h=max(lp.h,rp.h)+1
    return np

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalance(root).flag:
    print('yes')
else:
    print('not')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if isBalance(root).flag:
    print('Tree is balanced')
else:
    print('Tree is not balanced')