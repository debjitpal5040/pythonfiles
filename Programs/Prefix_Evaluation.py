n="+ - + 7 * 4 9 * 5 2 3"
arr=n.split()
stack=[]
for i in arr[::-1]:
    if i.lstrip('-').isnumeric():
        stack.append(i)
    else:
        a=stack.pop()
        b=stack.pop()
        exp=str(eval(a+i+b))
        stack.append(exp)
print(stack.pop())