# there must be a constant difference between the x values
def fact(p):
    for i in range(1, p + 1):
        p *= i
    return p


def v_cal(v, n):
    for i in range(1, n):
        v *= (v + i)
    return v


x = [0, 1, 2, 3]
y = [1, 2, 4, 8]
n = len(x)
h = x[1]-x[0]
Y = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    Y[i][0] = y[i]
for i in range(1, n):
    for j in range(n-1, i-1, -1):
        Y[j][i] = Y[j][i-1]-Y[j-1][i-1]
print("The backward difference table is :\n")
for i in range(n):
    print(x[i], end="\t")
    for j in range(i+1):
        print(round(Y[i][j], 3), end="\t")
    print("")
value = 2.5
v = (value-x[n-1])/h
res = Y[n-1][0]
for i in range(1, n):
    res += v_cal(v, i)*Y[n-1][i]/fact(i)
print("\nThe value of interpolated function at", value, "is", round(res, 3))
