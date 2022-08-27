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

    def removeDuplicates(self):
        if self.head is None or self.head.next is None:
            return self.head
        temp=self.head
        h=[temp.data]
        while temp.next:
            if temp.next.data in h:
                temp.next=temp.next.next
            else:
                h.append(temp.next.data)
                temp=temp.next

# Start with the empty list
llist = LinkedList()  # object of class LinkedList
llist.head = Node(1)
second = Node(2)
llist.head.next = second
third = Node(2)
second.next = third
llist.tail = Node(1)
third.next = llist.tail
llist.printList()
llist.removeDuplicates()
llist.printList()