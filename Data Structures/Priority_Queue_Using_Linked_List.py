# A simple implementation of  Priority Queue using Singly Linked List
class PriorityQueueNode:
    def __init__(self, data, priority, next=None):
        self.data = data
        self.priority = priority
        self.next = next
# Implementation of Priority Queue
class PriorityQueue:
    def __init__(self):
        self.front = None
    # Method to check Priority Queue is Empty
    def isEmpty(self):
        return self.front == None
    # Method to add items in Priority Queue According to their priority value
    def push(self, value, priority):
        if self.isEmpty():
            self.front = PriorityQueueNode(value, priority)
        else:
            # Special condition check to see that first node priority value
            if self.front.priority > priority:
                newNode = PriorityQueueNode(value, priority)
                newNode.next = self.front
                self.front = newNode
            else:
                # Traversing through Queue until it finds the next smaller priority node
                temp = self.front
                while temp.next:
                    # If same priority node found then current node will come after previous node
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                newNode = PriorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode
    # Method to remove high priority item from the Priority Queue
    def pop(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front = self.front.next
    # Method to return high priority node value Not removing it
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print(self.front.data)
    # Method to Traverse through Priority Queue
    def traverse(self):
        if self.isEmpty() == True:
            print("Queue is Empty!")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

pq = PriorityQueue()
pq.push(14, 2)
pq.push(11, 3)
pq.push(12, 0)
pq.push(17, 1)
pq.traverse()
pq.peek()
pq.pop()
pq.traverse()
pq.peek()
