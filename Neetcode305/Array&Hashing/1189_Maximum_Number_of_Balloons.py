class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        countT = Counter(text)
        balloon = Counter('balloon')

        res = len(text)
        for i in balloon:
            res = min(res, countT[i] // balloon[i])
        return res
