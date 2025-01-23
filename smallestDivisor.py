threshold = 6
nums = [1,2,5,9]

def check(divisor):
    cum = 0
    for num in nums:
        cum += num // divisor
        if num % divisor != 0:
            cum += 1
    return cum <= threshold
        
left = 1
right = ( max(nums)*len(nums) // threshold ) + 1
        
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)