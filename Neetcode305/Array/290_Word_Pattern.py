class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        pa = [*pattern]
        # https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
        st = s.split(" ")
        if len(pa) != len(st):
            return False
        paD = {}
        stD = {}

        for p1, s1 in zip(pa, st):
            if ((p1 in paD and paD[p1] != s1)
                    or (s1 in stD and stD[s1] != p1)):
                return False
            paD[p1] = s1
            stD[s1] = p1

        return True
