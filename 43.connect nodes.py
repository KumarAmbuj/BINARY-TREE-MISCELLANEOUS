class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None

def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def connect(node):
    queue=Queue()
    prev=None
    Enqueue(queue,node)
    Enqueue(queue,None)
    l=[]

    while(Size(queue)>1):

        rem=Dequeue(queue)
        if rem==None:
            prev=None
            Enqueue(queue,None)
        else:
            print(rem.val,end=' ')

            if prev == None:
                prev = rem
                l.append(rem)
            else:
                prev.next = rem
                prev = rem

            if rem.left:
                Enqueue(queue,rem.left)
            if rem.right:
                Enqueue(queue,rem.right)
    print()
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






