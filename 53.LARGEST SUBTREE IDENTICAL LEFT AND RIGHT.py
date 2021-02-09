class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def findnode(node,Str,maxsize,maxnode):
    if node==None:
        return 0

    left=['']
    right=['']
    ls=findnode(node.left,left,maxsize,maxnode)
    rs=findnode(node.right,right,maxsize,maxnode)

    size=ls+rs+1
    if left[0]==right[0]:
        if size>maxsize[0]:
            maxsize[0]=size
            maxnode[0]=node
    Str[0]=left[0]+str(node.val)+right[0]

    return size



def largestidentical(node):

    Str=['']
    maxsize=[0]
    maxnode=[None]
    findnode(node,Str,maxsize,maxnode)
    print(maxnode[0].val,maxsize[0])
    

root = Node(50)
root.left = Node(10)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(70)
root.right.left.left = Node(65)
root.right.left.right = Node(80)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)



largestidentical(root)
