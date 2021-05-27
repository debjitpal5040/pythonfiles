print("This is a demo program for Newton-Raphson method")
# Finding approximate roots of given function f(x)=3x^3-9x^2+8
def f(x):
    return 3*x**3-9*x**2+8
# g is the derivative of f w.r.t x
def g(x):
    return 9*x**2-18*x
i=0
a=-1;b=1;c=3
while i<10:
    a1=a-(f(a)/g(a))
    b1=b-(f(b)/g(b))
    c1=c-(f(c)/g(c))
    a=a1;b=b1;c=c1
    i+=1
print("First approximate root :",a)
print("Second approximate root :",b)
print("Third approximate root :",c)