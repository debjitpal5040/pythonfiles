def proterm(i, value, x):
    pro = 1
    for j in range(i):
        pro *= (value - x[j])
    return pro


x = [0, 1, 2, 5]
y = [2, 3, 12, 147]
n = len(x)
Y = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    Y[i][0] = y[i]
for i in range(1, n):
    for j in range(n - i):
        Y[j][i] = ((Y[j][i - 1] - Y[j + 1][i - 1]) / (x[j] - x[i + j]))
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(round(Y[i][j], 3), end="\t")
    print("")
value = 3
res = Y[0][0]
for i in range(1, n):
    res += proterm(i, value, x) * Y[0][i]
print("\nThe value of interpolated function at", value, "is", round(res, 3))
