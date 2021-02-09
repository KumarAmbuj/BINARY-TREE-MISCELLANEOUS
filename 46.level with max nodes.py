class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def Queue():
    queue=[]
    return queue
def Enqueue(queue,z):
    queue.append(z)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


def levelmaxnode(node):
    queue=Queue()
    Enqueue(queue,node)
    Enqueue(queue,None)
    level=0
    maxlevel=0

    count=0
    maxcount=0

    while(Size(queue)>1):
        rem=Dequeue(queue)

        if rem==None:
            Enqueue(queue,None)
            if count>maxcount:
                maxcount=count
                maxlevel=level
            count=0
            level += 1
        else:

            count+=1
            if rem.left:
                Enqueue(queue,rem.left)
            if rem.right:
                Enqueue(queue,rem.right)

    print(maxlevel)


root = Node(2)
root.left     = Node(1)
root.right     = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(8)
root.left.right.left = Node(5)

levelmaxnode(root)


