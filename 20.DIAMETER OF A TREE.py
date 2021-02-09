class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Pair:
    def __init__(self,dia=0,h=0):
        self.dia=0
        self.h=h

def Diameter(node):
    if node==None:
        np=Pair(0,-1)
        return np

    lp=Diameter(node.left)
    rp=Diameter(node.right)

    np=Pair()

    dia=lp.h+rp.h+2
    np.dia=max(dia,lp.dia,rp.dia)
    np.h=max(lp.h,rp.h)+1
    return np


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

node=Diameter(root)
print(node.dia)