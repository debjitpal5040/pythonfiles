s = []
front = -1
rear = -1
size = 3


def isEmpty(s):
    if front == rear:
        print("Empty Queue")
    else:
        print("Not Empty Queue")


def isFull(s):
    if rear == size-1:
        print("Full Queue")
    else:
        print("Not Full Queue")


def enqueue(s, item):
    global rear
    if rear == size-1:
        print("Overflow error, Queue is full")
        print("Maximum size of the Queue is :", size)
    else:
        rear += 1
        s.append(item)
        print(f"{item} enqueued to Queue")


def dequeue(s):
    global front
    if front == rear:
        print("Underflow error, Queue is empty")
    else:
        front += 1
        print("Dequed element is :", s[front])
        s[front] = None


def peek(s):
    if front == rear:
        print("Queue is empty")
    else:
        print("Top element is :", s[front])


def display(s):
    if front == rear:
        print("Queue is empty")
    else:
        print("The Queue is :", s)


enqueue(s, 'H')
enqueue(s, 'E')
peek(s)
enqueue(s, 'L')
display(s)
isFull(s)
enqueue(s, 'L')
display(s)
dequeue(s)
display(s)
dequeue(s)
display(s)
dequeue(s)
isEmpty(s)
display(s)
