nums = [0,1,2,4,5,7]

ans = []
start = nums[0]
curr = start
        
for i in range(1, len(nums)):
    if curr + 1 != nums[i]:
        if curr != start:
            ans.append(str(start) + "->" + str(curr))
        else:
            ans.append(str(start))
        start = nums[i]
        curr = nums[i]
    else:
        curr += 1
    
if curr != start:
    ans.append(str(start) + "->" + str(curr))
else:
    ans.append(str(start))

print(ans)
