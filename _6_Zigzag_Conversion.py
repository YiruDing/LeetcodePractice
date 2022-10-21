# https://www.youtube.com/watch?v=Q2Tw6gcVEwc
# 微軟面試
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ''

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            # 此為每個字母的起始間隔，隨著zigzag往下或往上，都會動態調整
            # Gotta go all the way down and up again
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1
                        and (i + increment - 2 * r) < len(s)):
                    # r本來在0~numRows - 1的範圍，r > 0 and r < numRows - 1
                    res += s[i + increment - 2 * r]
                    # V shape...decrease by 2 each time

    # 6:58 Each jump is going to be decreasing by 2

        return res


# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# increment：4

# r: 0 i: 0 res: P
# r: 0 i: 4 res: PA
# r: 0 i: 8 res: PAH
# r: 0 i: 12 res: PAHN

# r: 1 i: 1 res: PAHNAP
# r: 1 i: 5 res: PAHNAPLS
# r: 1 i: 9 res: PAHNAPLSII
# r: 1 i: 13 res: PAHNAPLSIIG

# r: 2 i: 2 res: PAHNAPLSIIGY
# r: 2 i: 6 res: PAHNAPLSIIGYI
# r: 2 i: 10 res: PAHNAPLSIIGYIR

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# increment：6

# r: 0 i: 0 res: P
# r: 0 i: 6 res: PI
# r: 0 i: 12 res: PIN
# r: 1 i: 1 res: PINAL
# r: 1 i: 7 res: PINALSI
# r: 1 i: 13 res: PINALSIG
# r: 2 i: 2 res: PINALSIGYA
# r: 2 i: 8 res: PINALSIGYAHR
# r: 3 i: 3 res: PINALSIGYAHRP
# r: 3 i: 9 res: PINALSIGYAHRPI
