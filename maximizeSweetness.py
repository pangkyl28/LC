# INPUTS
sweetness = [5,6,7,8,9,1,2,3,4]
k = 8

def check(target):
    # check if you can make k+1 piles where min sum is target
    total = 0
    curr = 0
    for num in sweetness:
        curr += num
        if curr >= target:
            curr = 0
            total += 1
    return total >= k+1
        



left = min(sweetness)
right = sum(sweetness) // (k+1)

while left < right:
    mid = (left + right + 1) // 2
    if check(mid):
        left = mid
    else:
        right = mid - 1
print(left)