class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            # 1 row/time
            for i in range(right - left):
                # Why right-left?
                # Ｃause we are dealing with the range that would shrink by 2 comparing to the outter row...
                # 處理的是二者的差，方形的框 然後再慢慢縮緊這個框架...
                top = left
                bottom = right
                topLeft = matrix[top][left + i]
                # store the value(which starts with[0][0]) so we can start to move

                matrix[top][left + i] = matrix[bottom - i][left]
                # 左上的位置(which starts with[0][0]) ＝ 原本左下的值(which starts with[len(matrix) - 1][0])
                # reassign the value

                matrix[bottom - i][left] = matrix[bottom][right - i]
                #  左下的位置(which starts with[len(matrix) - 1][0]) ＝ 原本右下的值(which starts with[len(matrix) - 1][len(matrix) - 1])

                matrix[bottom][right - i] = matrix[top + i][right]
                # 右下的位置(which starts with[len(matrix) - 1][len(matrix) - 1]) ＝原本右上的值(which starts with[0][len(matrix) - 1])

                matrix[top + i][right] = topLeft
                # 右上的位置(which starts with[0][len(matrix) - 1])=原本左上的值

            #!!!Then deal with the inner square with a smaller height as well as the width
            right -= 1
            left += 1
        # result=[['a'*len(matrix)]*len(matrix[0])]

        # for i in range(len(matrix)-1,-1,-1):
        #     for j in range(len(matrix[0])):
        #         while result:
        #             result.append()


# Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# left起始值為0,right為3,i為0,1,2,
# topLeft位置分別為[0][0],[0][2],[0][1]
#然後left為1,right為2,i為0
# topLeft位置為[1][1]
# topLeft:  1
# topLeft:  2
# topLeft:  3
# topLeft:  6