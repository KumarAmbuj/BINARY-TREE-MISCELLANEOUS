class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def maxbend(node,res,count,maxcount):
    if node==None:
        return

    if len(res)>1:
        if res[-1]!=res[-2]:
            count+=1
    if node.left==None and node.right==None:
        maxcount[0]=max(maxcount[0],count)

        return

    maxbend(node.left,res+'L',count,maxcount)
    maxbend(node.right,res+'R',count,maxcount)
def findmaxbends(node):
    res=''
    count=0
    maxcount=[0]
    maxbend(node,res,count,maxcount)
    print(maxcount[0])

root = newNode(10)
root.left = newNode(8)
root.right = newNode(2)
root.left.left = newNode(3)
root.left.right = newNode(5)
root.right.left = newNode(2)
root.right.left.right = newNode(1)
root.right.left.right.left = newNode(9)
findmaxbends(root)