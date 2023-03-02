# 這題有點廢到笑，但是屬於234的follow-up，故暫置此


class Solution:

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]