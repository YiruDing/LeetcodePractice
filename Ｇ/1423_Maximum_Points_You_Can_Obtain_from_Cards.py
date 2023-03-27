# Neetcode 2021最常問的問題

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(res, total)
            r += 1
            l += 1
        return res