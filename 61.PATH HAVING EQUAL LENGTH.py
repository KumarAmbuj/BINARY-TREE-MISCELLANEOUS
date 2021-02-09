class newnode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findnode(node,l,hash):
    if node==None:
        return

    if node.left==None and node.right==None:
        if l not in hash:
            hash[l]=0
        hash[l]+=1

    findnode(node.left,l+1,hash)
    findnode(node.right,l+1,hash)

def findpath(node):
    hash={}
    findnode(node,0,hash)

    for x in hash:
        print('{} path having length {}'.format(hash[x],x))

root = newnode(8)
root.left = newnode(5)
root.right = newnode(4)
root.left.left = newnode(9)
root.left.right = newnode(7)
root.right.right = newnode(11)
root.right.right.left = newnode(3)
findpath(root)
