n="7 4 9 * + 5 2 * - 3 +"
arr=n.split()
stack=[]
for i in arr:
    if i.lstrip('-').isnumeric():
        stack.append(i)
    else:
        a=stack.pop()
        b=stack.pop()
        exp=str(eval(b+i+a))
        stack.append(exp)
print(stack.pop())