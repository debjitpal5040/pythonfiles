
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

    def enqueue(self, item):
        if self.front == -1:
            self.rear = 0
            self.front = 0
            self.head = Node(item)
            self.tail = self.head
            print(f"{item} enqueued to Queue")
        elif (self.rear+1) % self.size == self.front:
            print("Overflow error, Queue is full")
            print("Maximum size of the Queue is :", self.size)
        else:
            self.rear = (self.rear+1) % self.size
            self.tail.next = Node(item)
            self.tail = self.tail.next
            print(f"{item} enqueued to Queue")

    def dequeue(self):
        if self.front == -1:
            print("Underflow error, Queue is empty")
        elif self.front == self.rear:
            print("Dequed element is :", self.head.data)
            self.head = None
            self.tail = None
            self.front = -1
            self.rear = -1
        else:
            print("Dequed element is :", self.head.data)
            self.head = self.head.next
            self.front = (self.front+1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        elif (self.rear >= self.front):
            print("The Queue is :", end=" ")
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The Queue is :", end=" ")
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


MyQueue = Queue(5)
MyQueue.enqueue(1)
MyQueue.display()
MyQueue.enqueue(2)
MyQueue.display()
MyQueue.enqueue(3)
MyQueue.display()
MyQueue.enqueue(4)
MyQueue.display()
MyQueue.enqueue(5)
MyQueue.display()
MyQueue.dequeue()
MyQueue.display()
MyQueue.dequeue()
MyQueue.display()
MyQueue.enqueue(6)
MyQueue.display()
MyQueue.enqueue(7)
MyQueue.display()
MyQueue.dequeue()
MyQueue.display()
MyQueue.enqueue(8)
MyQueue.display()
MyQueue.enqueue(9)
