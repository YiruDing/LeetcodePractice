# https://www.youtube.com/watch?v=V6Z3FTGhGwk


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = 0, len(matrix[0]) - 1

        while COL >= 0 and ROW <= len(matrix) - 1:
            num = matrix[ROW][COL]
            if num == target:
                return True
            if num > target:
                COL -= 1
            else:
                ROW += 1

        return False
