weights=[4,3,2,1]
profits=[1,2,3,4]
n=len(weights)
W=7
t=[[None for i in range(W+1)] for j in range(n+1)]
for i in range(n+1):
    t[i][0]=0
for j in range(W+1):
    t[0][j]=0
for i in range(1,n+1):
    for j in range(1,W+1):
        if weights[i-1]<=j:
            t[i][j] = max(profits[i-1]+t[i-1][j-weights[i-1]],t[i-1][j])
        else:
            t[i][j] = t[i-1][j]
print("Weights :",weights)
print("Profits :",profits)
print("W :",W)
print("Matrix[i][j] represents maximum profit can be obtained with weights = weights[:i] and W = j")
for i in range(n+1):
    for j in range(W+1):
        print(t[i][j],end=" ")
    print()
print("Maximum Profit :",t[n][W])