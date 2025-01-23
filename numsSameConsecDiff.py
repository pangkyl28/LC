# INPUTS 
n = 3
k = 7

def backtrack(curr):
    if len(curr) == n:
        ans.append(int(curr))
    else:
        lower = int(curr[-1]) - k
        upper = int(curr[-1]) + k
        if lower >= 0:
            temp = curr + str(lower)
            backtrack(temp)
        if upper <= 9:
            temp = curr + str(upper)
            backtrack(temp)
        
ans = []
for i in range(1, 10):
    backtrack(str(i))
print(ans)