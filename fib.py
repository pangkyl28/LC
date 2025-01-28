# INPUT
n = 2
# CODE
nums = [0]*(n+1)
if len(nums) > 1:
    nums[1] = 1
for i in range(2, len(nums)):
    nums[i] = nums[i-1] + nums[i-2]
print(nums[-1])