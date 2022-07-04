
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, size, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == self.rear:
            print("Empty Queue")
        else:
            print("Not Empty Queue")

    def isFull(self):
        if self.rear == self.size-1:
            print("Full Queue")
        else:
            print("Not Full Queue")

    def enqueue(self, data):
        if self.rear == self.size - 1:
            print("Overflow error, Queue is full")
            print("Maximum size of the Queue is :", self.size)
        else:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.rear += 1
            print(f"{data} enqueued to Queue")

    def dequeue(self):
        if self.front == self.rear:
            print("Underflow error, Queue is empty")
        else:
            self.front += 1
            print("Dequed element is :", self.head.data)
            self.head = self.head.next

    def peek(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print("Top element is :", self.head.data)

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


MyQueue = Queue(3)
MyQueue.enqueue(1)
MyQueue.enqueue(2)
MyQueue.enqueue(3)
MyQueue.enqueue(4)
MyQueue.isFull()
MyQueue.display()
MyQueue.peek()
MyQueue.dequeue()
MyQueue.display()
MyQueue.isEmpty()
MyQueue.peek()
MyQueue.enqueue(5)
