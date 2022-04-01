s = []
front = -1
rear = -1
size = 3


def isEmpty():
    if front == rear:
        print("Empty Queue")
    else:
        print("Not Empty Queue")


def isFull():
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
        print("Dequed element is :", s[0])
        s.pop(0)


def peek(s):
    if front == rear:
        print("Queue is empty")
    else:
        print("Top element is :", s[0])


def display(s):
    if front == rear:
        print("Queue is empty")
    else:
        print("The Queue is :", s)


enqueue(s, 1)
enqueue(s, 2)
enqueue(s, 3)
enqueue(s, 4)
isFull()
display(s)
peek(s)
dequeue(s)
display(s)
isEmpty()
peek(s)
enqueue(s, 5)
