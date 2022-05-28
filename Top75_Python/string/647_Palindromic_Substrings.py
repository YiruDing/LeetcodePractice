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
