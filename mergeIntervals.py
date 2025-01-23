# INPUT
intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key=lambda x: x[0])
curr = 0
while curr != len(intervals)-1:
    if intervals[curr][1] >= intervals[curr+1][0]:
        intervals[curr][1] = max(intervals[curr][1], intervals[curr+1][1])
        intervals.pop(curr+1)
    else:
        curr += 1

print(intervals)