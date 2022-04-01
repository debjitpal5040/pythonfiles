front = -1
rear = -1
size = 5
queue = [None for i in range(size)]


def enqueue(s, item):
    global front, rear
    if front == -1:
        rear = 0
        front = 0
        s[rear] = item
        print(f"{item} enqueued to Queue")
    elif (rear+1) % size == front:
        print("Overflow error, Queue is full")
        print("Maximum size of the Queue is :", size)
    else:
        rear = (rear+1) % size
        s[rear] = item
        print(f"{item} enqueued to Queue")


def dequeue(s):
    global front, rear
    if front == -1:
        print("Underflow error, Queue is empty")
    elif front == rear:
        print("Dequed element is :", s[front])
        front = -1
        rear = -1
    else:
        print("Dequed element is :", s[front])
        front = (front+1) % size


def display(s):
    if front == -1:
        print("Queue is Empty")
    elif (rear >= front):
        print("The Queue is :", end=" ")
        for i in range(front, rear + 1):
            print(s[i], end=" ")
        print()
    else:
        print("The Queue is :", end=" ")
        for i in range(front, size):
            print(s[i], end=" ")
        for i in range(rear + 1):
            print(s[i], end=" ")
        print()


enqueue(queue, 1)
display(queue)
enqueue(queue, 2)
display(queue)
enqueue(queue, 3)
display(queue)
enqueue(queue, 4)
display(queue)
enqueue(queue, 5)
display(queue)
dequeue(queue)
display(queue)
dequeue(queue)
display(queue)
enqueue(queue, 6)
display(queue)
enqueue(queue, 7)
display(queue)
dequeue(queue)
display(queue)
enqueue(queue, 8)
display(queue)
enqueue(queue, 9)
