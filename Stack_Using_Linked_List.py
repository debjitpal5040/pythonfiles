
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, size, head=None):
        self.head = head
        self.size = size
        self.length = 0

    def isempty(self):
        if self.length == 0:
            print("Empty Stack")
        else:
            print("Not Empty Stack")

    def isFull(self):
        if self.length == self.size:
            print("Full Stack")
        else:
            print("Not Full Stack")

    def push(self, data):
        if self.length < self.size:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            self.length += 1
            print(f'{data} pushed to stack')
        else:
            print("Overflow error, Stack is full")
            print("Maximum size of the stack is", self.size)

    def pop(self):
        if self.length != 0:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            self.length -= 1
            print("Poped element is :", poppednode.data)
        else:
            print("Underflow error, Stack is empty")

    def peek(self):
        if self.length == 0:
            print("Stack is empty")
        else:
            print("Top element of stack :", self.head.data)

    def display(self):
        iternode = self.head
        if iternode is None:
            print("Empty Stack")
        else:
            while iternode:
                print(iternode.data, end=" ")
                iternode = iternode.next
            print()


MyStack = Stack(3)
MyStack.display()
MyStack.push(1)
MyStack.isempty()
MyStack.push(2)
MyStack.peek()
MyStack.push(3)
MyStack.isFull()
MyStack.push(4)
MyStack.display()
MyStack.pop()
MyStack.pop()
MyStack.pop()
MyStack.display()
MyStack.pop()
MyStack.peek()
