# Finding approximate root of given function f(x)=2x-3cosx-1.85
print("This is a demo program for Regula Falsi method")
import math
def f(x):
    return 2*x-3*math.cos(x)-1.85
i=0;a=1;b=2
while i<5:
    x=(a*f(b)-b*f(a))/(f(b)-f(a))
    a=x
    i+=1
print("Approximate root :",x)