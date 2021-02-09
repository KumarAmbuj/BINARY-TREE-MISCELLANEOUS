class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findnode(node,l,count,maxcount):
    if node==None:
        return

    if len(l)==0:
        count=1
        l.append(node.val)
    else:
        l.append(node.val)
        if l[-1]-l[-2]==1:
            count+=1
    if node.left==None and node.right==None:
        maxcount[0]=max(count,maxcount[0])
        l.pop()
        return

    findnode(node.left,l,count,maxcount)
    findnode(node.right,l,count,maxcount)
    l.pop()


def countincreasing(node):

    l=[]
    count=0
    maxcount=[0]
    findnode(node,l,count,maxcount)
    print(maxcount[0])

root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(13)
root.left.right = Node(12)
root.right.left = Node(13)
root.right.right = Node(8)
countincreasing(root)