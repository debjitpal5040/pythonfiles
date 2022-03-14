# there must be a constant difference between the x values
def fact(p):
    for i in range(1, p + 1):
        p *= i
    return p


def u_cal(u, n):
    for i in range(1, n):
        u *= (u - i)
    return u


x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 2, 4, 8, 16, 32, 64]
n = len(x)
h = x[1]-x[0]
Y = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    Y[i][0] = y[i]
for i in range(1, n):
    for j in range(n-i):
        Y[j][i] = Y[j+1][i-1]-Y[j][i-1]
print("The forward difference table is :\n")
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(round(Y[i][j], 3), end="\t")
    print("")
value = 0.5
u = (value-x[0])/h
res = Y[0][0]
for i in range(1, n):
    res += u_cal(u, i)*Y[0][i]/fact(i)
print("\nThe value of interpolated function at", value, "is", round(res, 3))
