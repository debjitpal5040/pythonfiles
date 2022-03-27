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
            if (temp == self.head):
                break
        print()

    # Adding a node at the front of the list
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = self.tail
        self.tail.next = new_node
        self.head.prev = new_node
        self.head = new_node

# Adding a node at the end of the list
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = self.tail
        self.tail.next = new_node
        self.head.prev = new_node
        self.tail = new_node

    # Deleting a node from the beginning of the list

    def deleteFront(self):
        if self.head is None:
            print("The list is empty")
            return
        self.tail.next = self.head.next
        self.head = self.head.next
        self.head.prev = self.tail

    # Deleting a node from the end of the list
    def deleteEnd(self):
        if self.tail is None:
            print("The list is empty")
            return
        self.head.prev = self.tail.prev
        self.tail = self.tail.prev
        self.tail.next = self.head

    # Searching for a node in the list
    def search(self, data):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == data:
                return str(data) + " is present at position " + str(pos)
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        return str(data) + " is not present in the list"


# Start with the empty list
llist = LinkedList()  # object of class LinkedList
llist.head = Node(1)
second = Node(2)
llist.tail = Node(3)
llist.head.prev = llist.tail  # Link first node with the tail node
llist.head.next = second  # Link first node with second node
second.prev = llist.head  # Link second node with first node
second.next = llist.tail  # Link second node with last node
llist.tail.prev = second  # Link last node with second node
llist.tail.next = llist.head  # Link last node with first node
llist.printList()
llist.insertFront(0)
llist.printList()
llist.insertEnd(4)
llist.printList()
llist.deleteFront()
llist.printList()
llist.deleteEnd()
llist.printList()
print(llist.search(3))
