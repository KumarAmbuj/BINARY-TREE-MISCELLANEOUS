class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findmax(node,ans):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 1

    l=findmax(node.left,ans)
    r=findmax(node.right,ans)

    lmax=0
    rmax=0



    if node.left and ((node.left.val)==node.val+1):
        lmax=l+1
    if node.right and ((node.right.val)==node.val+1):

        rmax=r+1



    ans[0]=max(ans[0],lmax,rmax)
    return max(lmax,rmax)


def findmaxincreasing(node):
    ans=[-9]
    l=findmax(node,ans)
    print(ans[0])


root = newNode(6)
root.right = newNode(9)
root.right.left = newNode(7)
root.right.right = newNode(10)
root.right.right.right = newNode(11)

findmaxincreasing(root)