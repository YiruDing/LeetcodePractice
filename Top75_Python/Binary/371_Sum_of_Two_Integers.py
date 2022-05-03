# the solution that can't pass...
# https://leetcode.com/problems/sum-of-two-integers/discuss/776952/python-best-leetcode-371-explanation-for-python

# https://donic0211.medium.com/leetcode-371-sum-of-two-integers-33fbdefbe71f
# Not so good but workable


class Solution:

    def getSum(self, a, b):
        mask = 0xffffffff
        sum = (a ^ b) & mask
        carry = a & b
        while carry != 0:
            a = sum
            b = (carry << 1) & mask
            sum = (a ^ b) & mask
            carry = a & b
            # 0501
            # Why do we need to do it twice?
            # Is there any way not to repeat the code?
        if sum & 0x80000000:
            sum -= 0x100000000
        return sum