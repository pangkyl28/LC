from collections import defaultdict
import math
import heapq
# INPUTS
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

graph = defaultdict(list)
for _from, _to, _price in flights:
    graph[_from].append([_to, _price])
    
costs = [math.inf]*n
costs[src] = 0
heap = [(src, 0, 0)] # curr_loc, curr_cost, curr_stops

while heap:
    curr_loc, curr_cost, curr_stops = heapq.heappop(heap)
    if curr_cost > costs[curr_loc]:
        continue
    for nei, price in graph[curr_loc]:
        new_price = curr_cost + price
        if new_price < costs[nei] and curr_stops < k:
            costs[nei] = new_price
            heapq.heappush(heap, (nei, new_price, k+1))
ans = costs[dst] if costs[dst] < math.inf else -1
print(ans)