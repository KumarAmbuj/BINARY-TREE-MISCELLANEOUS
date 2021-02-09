def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(q):
    return len(q)



def findheight(arr):
    x=arr.index(-1)


    queue=Queue()
    Enqueue(queue,x)
    hash={}
    hash[x]=0
    while(Size(queue)):
        rem=Dequeue(queue)

        if rem in arr:

            x=arr.index(rem)
            hash[x]=hash[rem]+1

            Enqueue(queue,x)

            arr[x]=-1

            if rem in arr:

                z=arr.index(rem)
                arr[z]=-1
                Enqueue(queue,z)
                hash[z] = hash[rem] + 1

    h=0
    for x in hash:
        h=max(h,hash[x])
    print(h)

arr=[1, 5, 5, 2, 2, -1, 3]

findheight(arr)

arr=[-1, 0, 0, 1, 1, 3, 5]
findheight(arr)
