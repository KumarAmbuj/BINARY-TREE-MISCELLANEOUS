class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findnode(node,res,count,maxcount):
    if node==None:
        return


    x=str(node.val)
    if x not in res:
        res=res+x
        count+=1

    if node.left==None and node.right==None:
        maxcount[0]=max(maxcount[0],count)

    findnode(node.left,res,count,maxcount)
    findnode(node.right,res,count,maxcount)




def findmaxdistinct(node):

    res=''
    count=0
    maxcount=[0]

    findnode(node,res,count,maxcount)

    print(maxcount[0])

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)
root.right.right.right = newNode(9)
findmaxdistinct(root)