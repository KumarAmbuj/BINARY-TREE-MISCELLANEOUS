class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def check(node,hash,l):
    if node==None:
        return

    if l not in hash:
        hash[l]=1
    else:
        hash[l]+=1

    check(node.left,hash,l+1)
    check(node.right,hash,l+1)
def findwidth(node):
    hash={}
    check(node,hash,0)

    mx=0

    for x in hash:
        mx=max(mx,hash[x])
    print(mx)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
findwidth(root)