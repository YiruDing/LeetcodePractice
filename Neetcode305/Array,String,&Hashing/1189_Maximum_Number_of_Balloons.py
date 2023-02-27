class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        countT = Counter(text)
        balloon = Counter('balloon')

        res = len(text)
        for i in balloon:
            res = min(res, countT[i] // balloon[i])
        return res

# Intuitive Python Solution with O(n) time and O(1) space.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for char in text:
            if char in counter:
                counter[char] += 1
        counter["l"] //= 2
        counter["o"] //= 2
        return min(counter.values())