from collections import defaultdict
s = "ABAA"
k = 0

left = 0
right = 0
seen = defaultdict(int)
ans = 0
while right < len(s):
    # add rightmost to seen
    seen[s[right]] += 1

    # check if it is valid
    while (right - left + 1) - max(seen.values()) > k:
        # shift and remove left until valid
        seen[s[left]] -= 1
        left += 1

    ans = max(ans, right - left + 1)
    # move right up one and then continue
    right += 1
print(ans)