class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def bottom(node,hash,d,l):
    if node==None:
        return

    if d not in hash:
        hash[d]=[node.val,l]
    else:
        if hash[d][1]<=l:
            hash[d]=[node.val,l]
    bottom(node.left,hash,d-1,l+1)
    bottom(node.right,hash,d+1,l+1)

def bottomview(node):
    hash={}

    bottom(node,hash,0,0)

    arr=[]
    for x in hash:
        arr.append(x)

    arr=sorted(arr)
    for x in arr:
        print(hash[x][0],end=' ')

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
bottomview(root)
