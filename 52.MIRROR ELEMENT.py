class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def mirrornode(node,d,l,hash,parent):
    if node==None:
        return
    hash[node.val]=[d,l,parent,node]

    mirrornode(node.left,d-1,l+1,hash,node)
    mirrornode(node.right,d+1,l+1,hash,node)

def findmirror(node,k):
    hash={}

    mirrornode(node,0,0,hash,None)

    l=False
    r=False

    x=hash[k]
    parent=None
    if x[2]!=None:
        parent=x[2]

    if parent.left!=None and parent.left.val==k:
        l=True
    elif parent.right!=None and parent.right.val==k:
        r=True

    if parent!=None:
        val=hash[parent.val]

        for z in hash:

            if hash[z][0]==(-val[0]) and hash[z][1]==val[1]:

                if l==True:
                    if hash[z][3].right:
                        print('mirror of ',k,'is ',hash[z][3].right.val)
                    else:
                        print('mirror of {} is not present'.format(k))

                elif r==True:
                    if hash[z][3].left:
                        print('mirror of ',k,'is ',hash[z][3].left.val)
                    else:
                        print('mirror of {} not present'.format(k))









root = Node(1)
n1 = Node(2)
n2 = Node(3)
root.left = n1
root.right = n2
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
n1.left = n3
n2.left = n4
n2.right = n5
n6 = Node(7)
n7 = Node(8)
n8 = Node(9)
n3.right = n6
n4.left = n7
n4.right = n8
n9=Node(10)
n5.left=n9

findmirror(root,3)
findmirror(root,7)
findmirror(root,4)
findmirror(root,5)
