from collections import defaultdict
s = "ab"
t = "b"

have, need = defaultdict(int), defaultdict(int)
for c in t:
    need[c] += 1
total_needs = len(t)
total_haves = 0
l = 0
res = ""
# Assuming possible
for r in range(len(s)):
    while total_haves != total_needs:
        if l == len(s): # out of bound
            print(res)
            quit()
        # add s[l] to what we have
        have[s[l]] += 1
        # check if s[l] is something we need and that we are not overcounting
        if (s[l] in need) and have[s[l]] <= need[s[l]]:
            total_haves += 1
        # increase the sliding window
        l += 1
    # now that total_haves == total_needs, update res
    if (res == "") or (len(res) > (l - r)):
        res = s[r:l]
    # now we remove s[r] from what we know we have
    have[s[r]] -= 1
    if (s[r] in need) and have[s[r]] < need[s[r]]:
        total_haves -= 1
print(res)