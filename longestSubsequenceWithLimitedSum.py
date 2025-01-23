def solve(target):
    left, right = 0, len(pref_sum)-1
        
    while left <= right:
        mid = (left + right) // 2
        if pref_sum[mid] == target:
            return mid
        if target < pref_sum[mid]:
            right = mid - 1
        if target > pref_sum[mid]:
            left = mid + 1
    return left-1
# INPUTS
nums = [4,5,2,1]
queries = [3,10,21]
# CODE       
nums.sort()
pref_sum = [0] * (len(nums)+1)
for i in range(len(nums)):
    pref_sum[i+1] = pref_sum[i] + nums[i]
    
ans = []
for target in queries:
    ans.append(solve(target))
print(ans)