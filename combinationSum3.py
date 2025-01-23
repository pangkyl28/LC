#INPUT
k = 4
n = 1

def backtrack(curr):
    if sum(curr) == n and len(curr) == k:
        ans.append(curr[:])
    if len(curr) != k:
        if len(curr) == 0:
            x = 0
        else:
            x = curr[-1]
        for i in range(x+1, 10):
            if sum(curr) + i <= n:
                curr.append(i)
                backtrack(curr)
                curr.pop()

ans = []
backtrack([])
print(ans)