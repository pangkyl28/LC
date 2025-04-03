from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_seen = defaultdict(int)
        for c in s1:
            s1_seen[c] += 1

        seen = defaultdict(int)
        for i in range(len(s1)):
            seen[s2[i]] += 1
        for i in range(len(s1), len(s2)):
            # check if valid permutation
            if seen == s1_seen:
                return True
            # otherwise shift by 1
            seen[s2[i]] += 1
            seen[s2[i-len(s1)]] -= 1
            if seen[s2[i-len(s1)]] == 0:
                seen.pop(s2[i-len(s1)])
        if seen == s1_seen:
                return True
        else:
            return False

        
        