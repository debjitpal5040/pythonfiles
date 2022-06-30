weights=[4,3,2,1]
profits=[1,2,3,4]
n=len(weights)
W=7
t=[[-1 for i in range(W+1)] for j in range(n+1)]
def knapsack(weights,profits,n,W):
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]
    if weights[n-1]<=W:
        t[n][W]=max(profits[n-1]+knapsack(weights,profits,n-1,W-weights[n-1]),knapsack(weights,profits,n-1,W))
    else:
        t[n][W]=knapsack(weights,profits,n-1,W)
    return t[n][W]
print(knapsack(weights,profits,n,W))