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
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def deepest(node):

    queue=Queue()
    Enqueue(queue,node)
    Enqueue(queue,None)
    level=1

    res=1

    while(Size(queue)>1):
        rem=Dequeue(queue)

        if rem==None:
            level+=1
            Enqueue(queue,None)
        else:
            if level%2==1 and rem.left==None and rem.right==None:
                res=level

            if rem.left:
                Enqueue(queue,rem.left)
            if rem.right:
                Enqueue(queue,rem.right)
    print(res)


root = Node(10)
root.left = Node(28)
root.right = Node(13)
root.right.left = Node(14)
root.right.right = Node(15)
root.right.right.left = Node(23)
root.right.right.right = Node(24)
deepest(root)
