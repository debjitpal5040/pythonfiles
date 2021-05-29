# This is the program for implementation of Backward Interpolation
from math import factorial
def permutation(n,r):
    for m in range(1,r):
        n*=(n+m)
    return n
X=[1, 2, 3, 4, 5, 6, 7, 8]
Y=[[1,0,0,0,0,0,0,0],[8,0,0,0,0,0,0,0],[27,0,0,0,0,0,0,0],[64,0,0,0,0,0,0,0],[125,0,0,0,0,0,0,0],[216,0,0,0,0,0,0,0],[343,0,0,0,0,0,0,0],[512,0,0,0,0,0,0,0]]
x=7.5
h=X[1]-X[0]
n=len(X)
u=(x-X[n-1])/h
for i in range(1,n):
    for j in range(n-i,i-1,-1):
        Y[j][i]=Y[j][i-1]-Y[j-1][i-1]
Sum=Y[n-1][0]
for k in range(1,n):
    Sum+=(permutation(u,k)*Y[n-1][k])/factorial(k)
print(Sum)