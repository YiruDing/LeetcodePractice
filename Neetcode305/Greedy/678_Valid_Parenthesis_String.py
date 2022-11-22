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
            if leftMin < 0:  #s=(*)( 若無此兩行，恐以錯為對
                leftMin = 0
        return leftMin == 0

# https://leetcode.com/problems/valid-parenthesis-string/discuss/145228/python-using-stack-20ms-beats-100-probably-the-easiest-solution
# 好解答,但還沒認真看...
class Solution(object):
# The idea is, we firstly treat * as left (, then we need to make sure the left ( is always more than or equal to ).
# We can use a stack to do this.
# Then similarly, we treat * as a right ), we go through s from right to left, to make sure the right ) is always
# more than or equal to (. If both experiments succeed, then return True.

# O(n) time, O(n) space
def checkValidString(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # stack 1, try to test all the ( and * can balance all the )
    S=[]        
    # go through s from left to right
    for x in s:
        if x=='(' or x=='*':
            S.append(x)
        else:
            if len(S)>0:
                S.pop()
            else:
                return False        # this means left ( is not enough
    
    # stack 2, try to test all the ) and * can balance all the (
    S=[]        
    # go through s from right to left
    for x in s[::-1]:
        if x==')' or x=='*':
            S.append(x)
        else:
            if len(S)>0:
                S.pop()
            else:
                return False        # this means right ) is not enough
    
    return True