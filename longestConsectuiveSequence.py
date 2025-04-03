import heapq
nums = [0,3,7,2,5,8,4,6,0,1]

h = heapq.heapify(nums)
ans = 0
prev = heapq.heappop(nums)
count = 1
while nums:
    curr = heapq.heappop(nums)
    if curr == prev + 1:
        count += 1
    elif curr == prev:
        continue
    else:
        ans = max(ans,count)
        count = 1
    prev = curr
ans = max(ans,count)
print(ans)