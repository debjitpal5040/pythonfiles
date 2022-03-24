class Node: # Node class
	# Function to initialise the node object
	def __init__(self, data, next=None):
		self.data = data # instance attribute to store data
		self.next = next # instance attribute to store reference to next node

# Linked List class contains a Node object
class LinkedList:
	# Function to initialize head
	def __init__(self): # Constructor for linked list
		self.head = None
		self.tail = None
	# This function prints contents of linked list starting from head
	def printList(self): # instance method to print the list
		temp = self.head
		while (temp):
			print (temp.data, end=" ")
			temp = temp.next
		print()
	
	# Adding a node at the front of the list
	def insertFront(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	# Adding a node at the end of the list
	def insertEnd(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	
	# Adding a node after a given node
	def insertAfter(self, prev_node, new_data):
		if prev_node is None:
			print("The given previous node cannot be NULL")
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node
	
	# Adding a node before a given node
	def insertBefore(self, next_node, new_data):
		if next_node is None:
			print("The given next node cannot be NULL")
			return
		new_node = Node(new_data)
		node = self.head
		found = False
		while node is not None and not found:
			if node.next is next_node:
				found = True
				new_node.next = node.next 
				node.next = new_node
				break
			else:
				node = node.next
	
	# Deleting a node from the beginning of the list
	def deleteFront(self):
		if self.head is None:
			print("The list is empty")
			return
		self.head = self.head.next
	
	# Deleting a node from the end of the list
	def deleteEnd(self):
		if self.tail is None:
			print("The list is empty")
			return
		found = False
		node = self.head
		while node is not None and not found:
			if node.next is self.tail:
				found = True
				node.next = None
				self.tail = node
				break
			else:
				node = node.next
	
	# Deleting a given node from the list
	def delete(self, node):
		if node is None:
			return
		found = False
		nod = self.head
		while nod is not None and not found:
			if nod.next is node:
				found = True
				nod.next = node.next
				node.next = None
				break
			else:
				nod = nod.next

# Start with the empty list
llist = LinkedList() # object of class LinkedList
llist.head = Node(1)
second = Node(2)
llist.tail = Node(3)
llist.head.next = second # Link first node with second node
second.next = llist.tail # Link second node with the third node
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