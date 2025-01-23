import heapq
# Inputs
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

# Code
heap = [(-boxType[1], boxType[0]) for boxType in boxTypes]
heapq.heapify(heap)
        
ans = 0
total_boxes = 0
while total_boxes != truckSize and len(heap) > 0:
    numUnits, numBox = heapq.heappop(heap)
    numUnits = -numUnits
    if total_boxes + numBox <= truckSize:
        ans += numUnits*numBox
        total_boxes += numBox
    else:
        # total_boxes + numBox > truckSize
        ans += numUnits*(truckSize - total_boxes)
        total_boxes += (truckSize - total_boxes)
print(ans)