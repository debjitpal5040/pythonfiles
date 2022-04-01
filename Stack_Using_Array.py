s = []
size = 5


def isEmpty(a):
    if len(a) == 0:
        print("Empty Stack")
    else:
        print("Not Empty Stack")


def isFull(a):
    if len(a) == size:
        print("full stack")
    else:
        print("not full stack")


def push(a, i):
    if len(a) < size:
        print(f'{i} pushed to stack')
        a.insert(0, i)
    else:
        print("Overflow error, Stack is full")
        print("Maximum size of the stack is :", size)


def pop(a):
    if len(a) != 0:
        print("Poped element is :", a[0])
        a.pop(0)
    else:
        print("Underflow error, Stack is empty")


def peek(a):
    if len(a) != 0:
        print("Top element is :", a[0])
    else:
        print("Stack is empty")


def display(a):
    if len(a) == 0:
        print("Empty Stack")
    else:
        print("The stack is :", a)


display(s)
isEmpty(s)
push(s, 1)
push(s, 2)
display(s)
push(s, 3)
push(s, 4)
push(s, 5)
display(s)
push(s, 6)
pop(s)
display(s)
isFull(s)
pop(s)
display(s)
peek(s)
