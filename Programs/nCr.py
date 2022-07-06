# nCr demonstration
def combination(n, r):
    # since C(n, r) = C(n, n - r)
    if(r > n - r):
        r = n - r
    # initialize result
    res = 1
    # Calculate value of
    # [n * (n-1) *---* (n-r+1)] / [r * (r-1) *----* 1]
    for i in range(r):
        res *= (n - i)
        res /= (i + 1)
    return int(res)
n=int(input("Enter the value of n : "))
r=int(input("Enter the value of r : "))
print("The value of",str(n)+"C"+str(r),"is",combination(n,r))
""" 
Time Complexity = O(r)
Space Complexity = O(1)
"""