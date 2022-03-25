class Node:  # Node class
    # Function to initialise the node object
    def __init__(self, data, prev=None, next=None):
        self.data = data  # instance attribute to store data
        self.prev = prev  # instance attribute to store reference to previous node
        self.next = next  # instance attribute to store reference to next node


class LinkedList:
    # Function to initialize head
    def __init__(self):  # Constructor for the class
        self.head = None
        self.tail = None
    # This function prints contents of linked list starting from head

    def printList(self):  # instance method to print the list
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Adding a node at the front of the list
    def insertFront(self, new_data):
        new_node = Node(new_data)  # Allocate the Node & Put in the data
        new_node.next = self.head  # Make next of new node as head and previous as NULL
        if self.head is not None:  # change prev of head node to new node
            self.head.prev = new_node
        self.head = new_node  # move the head to point to the new node

    # Adding a node at the end of the list
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    # Adding a node after a given node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    # Adding a node before a given node
    def insertBefore(self, next_node, new_data):
        if next_node is None:
            print("The given next node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev.next = new_node
        next_node.prev = new_node

    # Deleting a node from the beginning of the list
    def deleteFront(self):
        if self.head is None:
            print("The list is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    # Deleting a node from the end of the list
    def deleteEnd(self):
        if self.tail is None:
            return
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None

    # Deleting a given node from the list
    def delete(self, node):
        if node is None:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    # Searching for a node in the list
    def search(self, data):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == data:
                return str(data) + " is present at position " + str(pos)
            temp = temp.next
            pos += 1
        return str(data) + " is not present in the list"


# Start with the empty list
llist = LinkedList()  # object of class LinkedList
llist.head = Node(1)
second = Node(2)
llist.tail = Node(3)
llist.head.next = second  # Link first node with second node
second.prev = llist.head  # Link second node with first node
second.next = llist.tail  # Link second node with last node
llist.tail.prev = second  # Link last node with second node
llist.printList()
llist.insertFront(0)
llist.printList()
llist.insertEnd(4)
llist.printList()
llist.insertAfter(llist.head, 5)
llist.printList()
llist.insertBefore(llist.tail, 6)
llist.printList()
llist.deleteFront()
llist.printList()
llist.deleteEnd()
llist.printList()
llist.delete(second)
llist.printList()
print(llist.search(1))