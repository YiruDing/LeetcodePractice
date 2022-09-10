# 1
class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


# 2
class Solution:

    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            left = right = i
            #for string of odd number
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            #for string of even number
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result

# oneliner,睡了一晚，9/10懂了ＸＤ
def countSubstrings(self, s):
    return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))