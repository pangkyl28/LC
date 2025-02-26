matrix = [[2,1,3],[6,5,4],[7,8,9]]

n = len(matrix)
dp = [[0 for i in range(n)] for i in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n):
        min_cost = dp[i+1][j]
        if j-1 != -1:
            min_cost = min(min_cost, dp[i+1][j-1])
        if j+1 != n:
            min_cost = min(min_cost, dp[i+1][j+1])
        dp[i][j] = min_cost + matrix[i][j]
print(min(dp[i]))