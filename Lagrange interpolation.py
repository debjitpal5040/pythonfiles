# This is a demo program for the implication of Lagrange interpolation
from functools import reduce
import operator
def interpolate(x, x_values, y_values):
    def _basis(j):
        p = [(x - x_values[m])/(x_values[j] - x_values[m]) for m in range(k) if m != j]
        return reduce(operator.mul, p)
    k = len(x_values)
    return sum(_basis(j)*y_values[j] for j in range(k))
X=[5,6,9,11]
Y=[12,13,14,16]
x=10
print(interpolate(x,X,Y))