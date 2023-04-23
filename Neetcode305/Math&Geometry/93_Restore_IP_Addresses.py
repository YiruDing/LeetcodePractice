class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        # 256 choices for each of the 4 spots. But the order of s stays same, we just place the '.' in between
        if len(s) < 4 or len(s) > 12:
            return []
        res = []

        def backtrack(i, dots, curIp):
            if dots == 4 and i == len(s):
                res.append(curIp[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != '0'):
                    # To avoit any leading zero:
                    # the length of the digit has to be exactly one or not start with 0
                    backtrack(j + 1, dots + 1, curIp + s[i:j + 1] + '.')

        backtrack(0, 0, '')
        return res