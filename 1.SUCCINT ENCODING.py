class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
def Peek(s):
    return s[-1]

class Pair:
    def __init__(self,node,s):
        self.node=node
        self.s=s

def encoding(node):

    stack=Stack()

    np=Pair(node,1)
    Push(stack,np)

    while(Size(stack)):
        top=Peek(stack)

        if top.s==1:
            print(1,end=' ')
            top.s+=1
            if top.node.left:
                np=Pair(top.node.left,1)
                Push(stack,np)
            else:
                print(0,end=' ')

        elif top.s==2:
            top.s += 1
            if top.node.right:
                np = Pair(top.node.right, 1)
                Push(stack, np)
            else:
                print(0,end=' ')


        elif top.s==3:
            x=Pop(stack)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
encoding(root)


