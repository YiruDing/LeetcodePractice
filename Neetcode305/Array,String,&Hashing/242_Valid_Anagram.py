# one line solution:
# return Counter(s)==Counter(t)
# return sorted(s)==sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # Build the hash map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            # 2/16 get(s[i],0) if there's no such character, return 0
        return True