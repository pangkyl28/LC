#INPUTS
nums = [7,2,5,10,8]
k = 2

def check(target):
    total = 0
    curr = 0
    for num in nums:
        if num > target:
            return False
        elif curr + num > target:
            total += 1
            curr = num
        else:
            curr += num
    if curr > 0:
        total += 1
    return total <= k

left = 0
right = sum(nums)
        
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)