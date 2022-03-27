class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == self.head):
                break
        print()

    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

    def deleteFront(self):
        if self.head is None:
            print("The list is empty")
            return
        self.tail.next = self.head.next
        self.head = self.head.next

    def deleteEnd(self):
        if self.tail is None:
            print("The list is empty")
            return
        node = self.head
        while node.next != self.tail:
            node = node.next
        self.tail = node
        self.tail.next = self.head

    def search(self, data):
        temp = self.head
        pos = 1
        while temp.next != self.head:
            if temp.data == data:
                return str(data) + " is present at position " + str(pos)
            temp = temp.next
            pos += 1
        return str(data) + " is not present in the list"


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
llist.tail = Node(3)
llist.head.next = second
second.next = llist.tail
llist.tail.next = llist.head
llist.printList()
llist.insertFront(0)
llist.printList()
llist.insertEnd(4)
llist.printList()
llist.deleteFront()
llist.printList()
llist.deleteEnd()
llist.printList()
print(llist.search(5))
