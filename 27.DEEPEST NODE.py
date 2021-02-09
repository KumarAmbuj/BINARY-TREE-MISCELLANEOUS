class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def deepestnode(node):
    queue=Queue()
    res=node
    Enqueue(queue,node)

    while(Size(queue)):

        rem=Dequeue(queue)

        res=rem

        if rem.left:
            Enqueue(queue,rem.left)
        if rem.right:
            Enqueue(queue,rem.right)

    print(res.val)

root = Node(1)
root.left = Node(2) 
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.right = Node(8)
root.right.left.right.left = Node(9)
deepestnode(root)
