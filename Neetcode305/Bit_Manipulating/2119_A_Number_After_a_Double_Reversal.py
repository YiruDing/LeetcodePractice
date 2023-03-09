# 1
class Solution(object):

    def isSameAfterReversals(self, num):
        # All you have to do is check the Trailing zeros
        return num == 0 or num % 10  # num % 10 means num % 10 != 0


# 2
def isSameAfterReversals(self, num: int) -> bool:
    return str(num) == str(num)[::-1].lstrip('0')[::-1] or num == 0
