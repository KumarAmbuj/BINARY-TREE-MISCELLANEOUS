class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(node):
    if node:
        print(node.val,end=' ')
        inorder(node.left)
        inorder(node.right)

def printnode(node,l,parent,hash):

    if node:
        if parent==None:
            print('-->{}'.format(node.val))
            hash[node]=4

        elif parent!=None:
            x=hash[parent]
            hash[node]=x+4

            for i in range(1,x+1):
                if i%4==0:
                    print('|',end='')
                else:
                    print(' ',end='')
            print('-->{}'.format(node.val))

        printnode(node.left,l+1,node,hash)
        printnode(node.right,l+1,node,hash)



def construct(arr):
    hash={}
    roots=[]

    for x in arr:
        l=x.split()

        if l[0] not in hash:
            root=Node(l[0])
            roots.append(root)
            hash[l[0]]=root

            newnode=Node(l[1])
            hash[l[1]]=newnode
            root.left=newnode

        elif l[0] in hash :
            node=hash[l[0]]
            newnode=Node(l[1])

            hash[l[1]]=newnode

            if node.left==None:
                node.left=newnode
            elif node.right==None:
                node.right=newnode


    i=0
    for x in roots:
        print('=====forest {}===='.format(i+1))
        i+=1
        hash={}
        printnode(x,0,None,hash)





links = ["a b", "a g", "b c", "c d", "d e", "c f",
                            "z y", "y x", "x w"]

construct(links)


links1 = ["a b", "b c", "b d", "a e"]

construct(links1)








