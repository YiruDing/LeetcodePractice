# https://www.youtube.com/watch?v=9UtInBqnCgA

# One Line Solution:
#    return Counter(s) == Counter(t)
#    return sorted(s) == sorted(t)


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # Only check the nums of the letters in "s"
            # Build the hash map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # If the key is not in hashmap yet, the default value will be 0(to be added 1)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            # get(s[i],0) if there's no such character, return 0
        return True
