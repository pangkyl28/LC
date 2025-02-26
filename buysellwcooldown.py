prices = [1]

# SOLUTION

n = len(prices)

hold = [0]*n
free = [0]*n
cd = [0]*n

hold[0] = -prices[0]

for i in range(1, n):
    hold[i] = max(hold[i-1], cd[i-1]-prices[i])
    free[i] = max(free[i-1], hold[i-1]+prices[i])
    cd[i] = free[i-1]
print(free[-1])
