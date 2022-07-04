# convergence achieved iff
# A is symmetric positive-definite, or
# A is strictly or irreducibly diagonally dominant
import numpy as np
A = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [4, 7, 3]
x = [0, 0, 0]
iterations = 15
L = [[0 for i in range(len(A))] for j in range(len(A))]
U = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A)):
    for j in range(i+1):
        L[i][j] = A[i][j]
    for k in range(i+1, len(A)):
        U[i][k] = A[i][k]
L_inverse = np.linalg.inv(L)
C = np.dot(L_inverse, b)
for i in range(iterations):
    T = np.dot(np.dot(L_inverse, U), x)
    x = C - T
    x = list(map(lambda p: round(p, 4), x))
    print(x)
