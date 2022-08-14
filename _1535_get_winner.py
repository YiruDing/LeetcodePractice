# https://maxming0.github.io/2020/08/03/Find-the-Winner-of-an-Array-Game/


# 此解頗優
# https://github.com/wisdompeak/LeetCode/blob/master/Greedy/1535.Find-the-Winner-of-an-Array-Game/1535.Find-the-Winner-of-an-Array-Game.cpp
class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        curMax = arr[0]
        win = 0
        for i in range(1, n):
            if arr[i] > curMax:
                curMax = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return curMax