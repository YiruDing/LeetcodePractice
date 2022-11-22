class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            #    Get every i in the top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            print("result: ",result)
            #    Get every i in the right column
            for i in range(top, bottom):
                # top剛加一，所以可以這樣用
                result.append(matrix[i][right - 1])
            right -= 1
            print("result: ",result)
            if not (left < right and top < bottom):
                break
            #    Get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            print("result: ",result)
            #    Get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            print("result: ",result)
        return result
# result:  [1, 2, 3]
# result:  [1, 2, 3, 6, 9]
# result:  [1, 2, 3, 6, 9, 8, 7]
# result:  [1, 2, 3, 6, 9, 8, 7, 4]
# result:  [1, 2, 3, 6, 9, 8, 7, 4, 5]
# result:  [1, 2, 3, 6, 9, 8, 7, 4, 5]