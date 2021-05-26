# Ackermann function demonstration
"""
It is one of the simplest and earliest-discovered examples of a 
total computable function that is not primitive recursive.
"""
print("This is the program for Ackermann function")
x,y=map(int,input("Please input the two arguments of the function : ").split())
def ackermann(m,n):
    try:
        if m==0 and n>=0:
            return n+1
        elif n==0 and m>0:
            return ackermann(m-1,1)
        elif m>0 and n>0:
            return ackermann(m-1,ackermann(m,n-1))
        else:
            return "Invalid Input"
    except:
        return "Too large calculation...beyond my limit"
print("Ackermann"+"("+str(x)+","+str(y)+")","=",str(ackermann(x,y)))
"""
Time Complexity = O(m*ackermann(m,n))
Space Complexity = O(m)
"""