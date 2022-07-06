def fractional_knapsack(profit, weight, capacity):
    # if sum of weights is <= capacity, then return sum of profits and take all whole weights
    if sum(weight)<=capacity:
        return sum(profit), [1]*len(profit)
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(profit)))
    # contains ratios of profits to weight
    ratio = [v/w for v, w in zip(profit, weight)]
    # index is sorted according to profit-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_profit = 0
    fractions = [0]*len(profit)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_profit += profit[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_profit += profit[i]*fractions[i]
            break

    return max_profit, fractions


n = int(input('Enter number of items : '))
profit = [int(v) for v in input(f'Enter the profits of the {n} item(s) in order : ').split()]
weight = [int(w) for w in input(f'Enter the weights of the {n} item(s) in order : ').split()]
capacity = int(input('Enter maximum weight of knapsack: '))
max_profit, fractions = fractional_knapsack(profit, weight, capacity)
print('The maximum profit of items that can be achieved :', max_profit)
print('The fractions in which the items should be taken :', fractions)
