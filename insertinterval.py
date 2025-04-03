# INPUTS
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [4,8]
# intervals = [[1,3],[6,9]] 
# newInterval = [2,5]

# use binary search to find where newinterval goes
left = 0
right = len(intervals)-1
while left <= right:
    middle = (left + right) // 2
    if intervals[middle][0] < newInterval[0]:
        left = middle + 1
    else:
        right = middle - 1
intervals.insert(left, newInterval)
#print(intervals)
ans = []
for start, end in intervals:
    if ans and start <= ans[-1][1]:
        ans[-1][1] = max(ans[-1][1], end)
    else:
        ans.append([start, end])
