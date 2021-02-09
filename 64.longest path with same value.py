class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def findpath(node,ans):
    if node==None:
        return 0

    left=findpath(node.left,ans)
    right=findpath(node.right,ans)

    lmax=0
    rmax=0

    if node.left and node.left.val==node.val:
        lmax=left+1
    if node.right and node.right.val==node.val:
        rmax=right+1

    ans[0]=max(ans[0],lmax+rmax)
    return max(lmax,rmax)


def longestpath(node):
    ans=[0]
    l=findpath(node,ans)
    print(ans[0])


root = newNode(4)
root.left = newNode(4)
root.right = newNode(4)
root.left.left = newNode(4)
root.left.right = newNode(9)
root.right.right = newNode(5)
longestpath(root)

