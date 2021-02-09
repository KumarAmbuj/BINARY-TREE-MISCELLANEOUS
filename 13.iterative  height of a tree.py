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

def height(node):

    queue=Queue()
    Enqueue(queue,node)
    Enqueue(queue,None)
    count=0
    while(Size(queue)>1):
        rem=Dequeue(queue)

        if rem==None:
            count+=1
            Enqueue(queue,None)
        else:
            if rem.left:
                Enqueue(queue,rem.left)
            if rem.right:
                Enqueue(queue,rem.right)
    print(count)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
height(root)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
height(root)



