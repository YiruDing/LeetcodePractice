# https://leetcode.com/problems/add-binary/solutions/279879/python-easy-to-understand/?q=python&orderBy=most_votes
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry //= 2

        return result[::-1]


#Neetcode
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0

        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0
            # ord(b[i]) - ord('0') 轉為integer
            # 亦可作int(a[i])

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            # 3/8 順序很重要！
            carry = total // 2

        if carry:
            res = '1' + res
            # 3/8 順序很重要！
        return res
