class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2)
                    or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True


# 以下解答不知何處出問題...
class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:

        checkS = {}
        checkT = {}

        def helper(string, dictionary):
            res = ''
            num = 0
            for i in range(len(string)):

                if s[i] not in dictionary:
                    num += 1
                    dictionary[s[i]] = str(num)

                res += dictionary[s[i]]

            return res

        resS = helper(s, checkS)
        resT = helper(t, checkT)
        print('resS:', resS)
        print('resT:', resT)

        return resS == resT
