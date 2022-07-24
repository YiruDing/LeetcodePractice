# https://maxming0.github.io/2020/08/03/Find-the-Winner-of-an-Array-Game/

class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        cur = arr[0]
        win = 0
        for i in range(1, n):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return cur