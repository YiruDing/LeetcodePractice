class Solution:

    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
                return 0
            res = (res * 10) + digit


# Other solution
class Solution:

    def reverse(self, x):
        if x < 0:
            return -1 * self.reverseUtil(-x)
        return self.reverseUtil(x)

    def reverseUtil(self, x):
        result = 0
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)

        return 0 if result > pow(2, 31) - 1 or result < -pow(2, 31) else result


# https://leetcode.com/problems/reverse-integer/discuss/132861/3-lines-Python-Solution
class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1, -1][x < 0]
# It is only a trick. which mean [1, -1][True] or [1, -1][False] as well as [1, -1][0] or [1, -1][1]
# we shoule use
# sign = 1 if x>0 else -1
# that is easy to understand

        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31) - 1 < rst < 2**31 else 0
