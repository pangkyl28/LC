# INPUTS
cost = [10, 15, 20]

def dp(i):
    if i == 0 or i == 1:
        return 0

    if i in states:
        return states[i]
    
    states[i] = min( dp(i-1) + cost[i-1], dp(i-2) + cost[i-2] )
    return states[i]

states = {}
print( dp(len(cost)) )