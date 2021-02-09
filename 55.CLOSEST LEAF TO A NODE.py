class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findnode(node,x,l):
    if node==None:
        return False

    if node.val==x:
        l.append(node)
        return True

    if findnode(node.left,x,l):
        l.append(node)
        return True

    if findnode(node.right,x,l):
        l.append(node)
        return True
    return False
def findleaf(node,d,block,count):
    if node==None:
        return
    if node==block:
        return

    if node.left==None and node.right==None:
        if count[0]>d:
            count[0]=d
        return

    findleaf(node.left,d+1,block,count)
    findleaf(node.right,d+1,block,count)



def findclosest(node,x):
    l=[]

    findnode(node,x,l)



    dist=99
    block=None
    for i in range(len(l)):

        if i==0:
            block=None
        else:
            block=l[i-1]
        count=[999]
        findleaf(l[i], 0, block, count)

        dist=min(dist,count[0]+i)

    print(dist)


root = newNode(1)
root.left = newNode(12)
root.right = newNode(13)

root.right.left = newNode(14)
root.right.right = newNode(15)

root.right.left.left = newNode(21)
root.right.left.right = newNode(22)
root.right.right.left = newNode(23)
root.right.right.right = newNode(24)

root.right.left.left.left = newNode(1)
root.right.left.left.right = newNode(2)
root.right.left.right.left = newNode(3)
root.right.left.right.right = newNode(4)
root.right.right.left.left = newNode(5)
root.right.right.left.right = newNode(6)
root.right.right.right.left = newNode(7)
root.right.right.right.right = newNode(8)

x = root.right.val
findclosest(root,x)
