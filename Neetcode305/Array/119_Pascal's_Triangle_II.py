class Solution:

    def getRow(rowIndex):
        pascal = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                pascal[j] += pascal[j - 1]
        return pascal


# input:3
# res [1, 2, 1, 1]
# res [1, 2, 3, 1]
# res [1, 3, 3, 1]

# My solution ...to be fixed


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1] * (i + 1) for i in range(rowIndex)]
        # 答案的長度為index + 1
        for i in range(rowIndex):
            # 要考慮到首尾的值不能變
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res[rowIndex]


# 另解
class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row