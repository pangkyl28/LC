# INPUTS
graph = [[1,2],[3],[3],[]]


def backtrack(curr):
    # base case
    if curr[-1] == n-1:
        ans.append(curr[:])
        
    for num in graph[curr[-1]]:
        if num not in curr:
            curr.append(num)
            backtrack(curr)
            curr.pop()


ans = []
n = len(graph)
backtrack([0])
print(ans)