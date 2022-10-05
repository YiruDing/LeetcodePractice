# My solution
# To be fixed...
# 思考以下不同的狀況，就會發現（和＊真的要分開處理
# (*)
# ＊）＊＊））
# (()))(
# class Solution:

#     def checkValidString(self, s: str) -> bool:
#         if len(s) <= 1:
#             return False

#         check = []
#         for i in range(len(s)):
#             if i == "）":
#                 if "（" not in check or "*" not in check:
#                     return False
#                 elif "（" in check or "*" in check:
#                     check.pop()
#             else:
#                 check.append(s[i])
#         return True if len(check) == 0 or (len(check) == 1
#                                            and check[0] == "*") else False


class Solution:

    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        # 8:49 leftMin, leftMax represent the range of possibilities...left=>left parenthesis
        # leftMax: The maxmum "(" we can have.(treat the 'wild card' as left parenthesis)
        # leftMin: The minimum "(" we can have.treat the 'wild card' as right parenthesis
        # !!!The result would be True if leftMin is 0
        # if leftMin<0 or leftMin<0, we got reset it/them to 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
                # Ignore/Use the wild card

            if leftMax < 0:
                return False
            if leftMin < 0:  #s=(*)( 若無此兩行，恐以真為假
                leftMin = 0
        return leftMin == 0
