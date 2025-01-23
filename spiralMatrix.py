# INPUT
matrix = [[3],[2]]

top, bottom = 0, len(matrix)-1
left, right = 0, len(matrix[0])-1

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
curr_row = 0
curr_col = 0

curr_dir = 0

ans = [0]*(len(matrix)*len(matrix[0]))
curr_index = 0

for i in range(len(ans)):
    ans[i] = matrix[curr_row][curr_col]

    if curr_dir == 0 and curr_col == right:
        curr_dir = 1
        top += 1
    elif curr_dir == 1 and curr_row == bottom:
        curr_dir = 2
        right -= 1
    elif curr_dir == 2 and curr_col == left:
        curr_dir = 3
        bottom -= 1
    elif curr_dir == 3 and curr_row == top:
        curr_dir = 0
        left += 1

    curr_row += directions[curr_dir][0]
    curr_col += directions[curr_dir][1]

print(ans)