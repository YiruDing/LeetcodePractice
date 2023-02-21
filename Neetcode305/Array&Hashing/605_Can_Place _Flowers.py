# Neetcode 1
class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):  #skip the first and the last
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
    
# Neetcode 2

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                # 2/21 此位置有花
                n -= int((empty - 1)/2) # int division, round toward zero
                # 2/21 ??
                empty = 0
            else:
                empty += 1
        n -= int(empty) // 2
        return n <= 0