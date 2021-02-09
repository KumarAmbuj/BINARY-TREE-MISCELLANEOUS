class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None

def check(node,hash,d,l):
    if node==None:
        return

    if d not in hash:
        hash[d]=node
        l.append(node)
    else:
        hash[d].next=node
        hash[d]=node
    check(node.left,hash,d+1,l)
    check(node.right,hash,d+1,l)
def connect(node):
    hash={}
    l=[]
    check(node,hash,0,l)

    for x in l:
        rem=x
        while(rem):
            print(rem.val,end=' ')
            rem=rem.next
        print()

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(90)
connect(root)