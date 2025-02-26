import collections

# INPUTS
s = "babad"

queue = collections.deque()
for i in range(len(s)):
    queue.append((i,i))
for i in range(len(s)-1):
    queue.append((i,i+1))       
longest = 0
while queue:
    left, right = queue.popleft()
    if s[left] == s[right]:
        longest = right - left + 1
        if left != 0 and right != len(s)-1:
            queue.append((left-1, right+1))
print(longest)