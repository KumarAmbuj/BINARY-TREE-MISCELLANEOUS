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


def deepnode(node):
    queue=Queue()
    l=[]
    level=0
    res=node
    Enqueue(queue,node)
    Enqueue(queue,None)
    while(Size(queue)>1):
        rem=Dequeue(queue)

        if level not in l:
            l.append(level)
            if rem.left==None and rem.right==None:
                res=rem


        if rem==None:
            level+=1
            Enqueue(queue,None)

        else:

            if rem.left:
                Enqueue(queue,rem.left)
            if rem.right:
                Enqueue(queue,rem.right)
    print(res.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.Left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.right = Node(8)
root.right.left.right.left = Node(9)
root.right.right.right.right = Node(10)
deepnode(root)




