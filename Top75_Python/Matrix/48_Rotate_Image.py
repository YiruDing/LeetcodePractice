class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                #                 ???   Why right-left
                # 處理的是二者的差，方形的框
                # 然後再慢慢縮緊這個框架...
                top = left
                bottom = right
                topLeft = matrix[top][left + i]
                # store the value so we can start to move

                matrix[top][left + i] = matrix[bottom - i][left]
                # 左下-->左上

                matrix[bottom - i][left] = matrix[bottom][right - i]
                # 右下-->左下

                matrix[bottom][right - i] = matrix[top + i][right]
                # 右上-->右下

                matrix[top + i][right] = topLeft
                # 右下-->左下

                # Then deal with the inner square
            right -= 1
            left += 1
        # result=[['a'*len(matrix)]*len(matrix[0])]

        # for i in range(len(matrix)-1,-1,-1):
        #     for j in range(len(matrix[0])):
        #         while result:
        #             result.append()
