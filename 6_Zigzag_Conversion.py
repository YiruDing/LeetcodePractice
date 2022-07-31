# https://www.youtube.com/watch?v=Q2Tw6gcVEwc
# 微軟面試
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ''

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            # Gotta go all the way down and up again
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1
                        and (i + increment - 2 * r) < len(s) < len(s)):
                    res += s[i + increment - 2 * r]

    # 6:58 Each jump is going to be decreasing by 2

        return res


# 待修的my solution
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         res=''
#         num=numRows
#         count=0
#         for i in range(len(s)):

#             while len(res)<len(s):
#                 while i/numRows==count:
#                     res+=s[i]
#                 count+=1

#             return res