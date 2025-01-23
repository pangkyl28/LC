# INPUTS
nums = [1,3,5,6]
target = 7
# CODE
left, right = 0, len(nums)-1
        
while left < right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
    print(mid)
    