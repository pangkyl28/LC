# INPUTS
s = "PAYPALISHIRING"
numRows = 4

arr = [["" for i in range(((len(s) // (2*(numRows - 1)) + 1)*2))] for j in range(numRows)]
curr_row = 0
curr_col = 0
direction = "down"
for c in s:
    arr[curr_row][curr_col] = c
    # move
    if (curr_row == numRows-1) and direction == "down":
        curr_row -= 1
        curr_col += 1
        direction = "up"
    elif (curr_row == 0) and direction == "up":
        curr_row += 1
        direction = "down"
    elif direction == "down":
        curr_row += 1
    elif direction == "up":
        curr_row -= 1
        curr_col += 1
ans = ""
for i in range(len(arr)):
    for j in range(len(arr[0])):
        ans = ans + arr[i][j]
print(ans)