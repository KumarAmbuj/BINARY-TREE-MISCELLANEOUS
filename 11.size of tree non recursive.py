class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Return size of tree
def sizeoftree(root):
    count=0
    if root == None:
        return 0
    q = []
    q.append(root)

    while (len(q) != 0):
        root = q.pop(0)
        count += 1
        if (root.left):
           q.append(root.left)

        if (root.right):
           q.append(root.right)
    print(count)

        
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

sizeoftree(root)

