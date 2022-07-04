def seidel(A, x, b):
    n = len(A)
    for i in range(n):
        d = b[i]
        for j in range(n):
            if(i != j):
                d -= A[i][j] * x[j]
        x[i] = d / A[i][i]
    return list(map(lambda p: round(p, 4), x))


A = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [4, 7, 3]
x = [0, 0, 0]
iterations = 15
for i in range(iterations):
    x = seidel(A, x, b)
    print(x)
