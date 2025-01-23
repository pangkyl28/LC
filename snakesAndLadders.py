from collections import deque 
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

line = []
for i in range(len(board)):
    if i % 2 == 0:
        line += board[len(board)-i-1]
    else:
        line += reversed(board[len(board)-i-1])
print(line)

queue = deque()
queue.append(0)
seen = set()
seen.add(0)
steps = 0
        
while queue:
    for i in range(len(queue)):
        curr = queue.popleft()
        if curr == len(line)-1:
            print(steps)
                
        for j in range(1, 7):
            next_tile = curr + j
            if next_tile > len(line)-1:
                continue
            if line[next_tile] != -1:
                next_tile = line[next_tile] - 1
            if next_tile not in seen:
                seen.add(next_tile)
                queue.append(next_tile)
                
    steps += 1
print(-1)
