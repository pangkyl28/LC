strs = ["flower","flow","flight"]

ans = ""
n = min(len(s) for s in strs)

for i in range(n):
    c = strs[0][i:i+1]
    all_same = True
    for s in strs:
        if s[i:i+1] != c:
            all_same = False
    if all_same == True:
        ans += c
    else:
        print(ans)
print(ans)