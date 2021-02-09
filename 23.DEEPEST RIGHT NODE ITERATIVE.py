class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


def rightmost(node):

    queue=Queue()
    Enqueue(queue,node)
    res=-1
    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.left:
            Enqueue(queue,rem.left)
        if rem.right:
            Enqueue(queue,rem.right)
            if rem.right.left==None and rem.right.right==None:
                res=rem.right.val
    print(res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)

root.right.left.right.right = Node(9)


rightmost(root)
