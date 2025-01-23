# INPUT
nums = [1,2,3,4]
# OUTPUT
# [24,12,8,6]

pref = [1]*len(nums)
suff = [1]*len(nums)

for i in range(1, len(nums)):
    pref[i] = nums[i-1] * pref[i-1]
for i in range(len(nums)-2, -1, -1):
    suff[i] = nums[i+1] * suff[i+1]

print([pref[i]*suff[i] for i in range(len(nums))])