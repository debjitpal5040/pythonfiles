# This is the program for implementation of Forward Interpolation
from math import factorial
def permutation(n,r):
    for m in range(1,r):
        n*=(n-m)
    return n
X=[0.5, 1.0, 1.5, 2.0, 2.5]
Y=[[0.22245,0,0,0,0], [0.25031,0,0,0,0], [0.27799,0,0,0,0], [0.30546,0,0,0,0], [0.33269,0,0,0,0]]
x=1.1
h=X[1]-X[0]
u=(x-X[0])/h
n=len(X)
for i in range(1,n):
    for j in range(n-i):
        Y[j][i]=Y[j+1][i-1]-Y[j][i-1]
Sum=Y[0][0]
for k in range(1,n):
    Sum+=(permutation(u,k)*Y[0][k])/factorial(k)
print(Sum)