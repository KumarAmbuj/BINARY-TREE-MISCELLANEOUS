class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def balance(node,k,res,d,l):
    if node==None:
        return

    if d==k:
        if len(l)==0:
            l.append(node.val)
        else:
            if node.val>l[-1]:
                res[0]=True
            else:
                res[0]=False
            l.append(node.val)
    balance(node.left,k,res,d-1,l)
    balance(node.right,k,res,d+1,l)

def isBalance(node,k):

    res=[False]
    l=[]
    balance(node,k,res,0,l)
    print(res[0])
root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(4)
root.left.right.left = Node(6)
isBalance(root,-1)
