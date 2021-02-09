class Node:
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


def findleaf(node,d,block,count,res):
    if node==None:
        return
    if node==block:
        return

    if node.left==None and node.right==None:
        if count[0]>d:
            count[0]=d
            res[0]=node.val
        return

    findleaf(node.left,d+1,block,count,res)
    findleaf(node.right,d+1,block,count,res)



def findclosest(node,x):
    l=[]

    findnode(node,x,l)



    dist=99
    block=None
    leaf = ''
    for i in range(len(l)):

        if i==0:
            block=None
        else:
            block=l[i-1]
        count=[999]
        res=['']

        findleaf(l[i], 0, block, count,res)

        if count[0]+i<dist:
            dist=count[0]+i
            leaf=res[0]

    print(leaf)


root = Node('A')
root.left = Node('B')
root.right = Node('C');
root.right.left = Node('E');
root.right.right  = Node('F');
root.right.left.left = Node('G');
root.right.left.left.left  = Node('I');
root.right.left.left.right = Node('J');
root.right.right.right  = Node('H');
root.right.right.right.left = Node('K');

k = 'H'
findclosest(root,k)

k = 'C'
findclosest(root,k)