from collections import defaultdict

# INPUTS
s = "anagram"
t = "nagaram"


letters = defaultdict(int)
for c in s:
    letters[c] += 1
for c in t:
    letters[c] -= 1
for key in letters.keys():
    if letters[key] != 0:
        print("False")
print("True")