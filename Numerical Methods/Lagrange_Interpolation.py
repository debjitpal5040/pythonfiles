x = [0, 1, 2, 5]
y = [2, 3, 12, 147]
n = len(x)
res = 0
value = 3
for i in range(n):
    p = 1
    q = 1
    for j in range(n):
        if j != i:
            p *= (value-x[j])
            q *= (x[i]-x[j])
    res += (p*y[i])/q
print("The value of interpolated function at", value, "is", round(res, 3))
