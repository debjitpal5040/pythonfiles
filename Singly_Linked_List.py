class Node:  # Node class
    # Function to initialise the node object
    def __init__(self, data, next=None):
        self.data = data  # instance attribute to store data
        self.next = next  # instance attribute to store reference to next node


class LinkedList:
    # Function to initialize head
    def __init__(self):  # Constructor for linked list
        self.head = None
        self.tail = None
    # This function prints contents of linked list starting from head

    def printList(self):  # instance method to print the list
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Adding a node as the head of the list
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Adding a node as the tail of the list
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        self.tail.next = new_node
        self.tail = new_node

    # Adding a node after a given middle node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Adding a node before a given middle node
    def insertBefore(self, next_node, new_data):
        if next_node is None:
            print("The given next node cannot be NULL")
            return
        new_node = Node(new_data)
        node = self.head
        while node.next != next_node:
            node = node.next
        new_node.next = node.next
        node.next = new_node

    # Deleting the head node from the list
    def deleteFront(self):
        if self.head is None:
            print("The list is empty")
            return
        self.head = self.head.next

    # Deleting the tail node from the list
    def deleteEnd(self):
        if self.tail is None:
            print("The list is empty")
            return
        node = self.head
        while node.next != self.tail:
            node = node.next
        node.next = None
        self.tail = node

    # Deleting a given middle node from the list

    def delete(self, node):
        if node is None:
            return
        nod = self.head
        while nod.next != node:
            nod = nod.next
        nod.next = node.next

    # Searching for a node in the list

    def search(self, data):
        temp = self.head
        pos = 1
        while temp:
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
second.next = llist.tail  # Link second node with the third node
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
llist.delete(llist.head.next.next)
llist.printList()
print(llist.search(6))
