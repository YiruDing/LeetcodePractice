# triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]-->True
# triplets = [[3,5,1],[10,5,7]] , target = [3,5,7]-->False


# 10/1 My solution
# To be fixed...
class Solution:

    def mergeTriplets(self, triplets: List[List[int]],
                      target: List[int]) -> bool:
        row, col = len(triplets), len(triplets[0])
        check = []

        for i in range(col):
            m = max(triplets[j][i] for j in range(row))
            check.append(m)

        for i in range(len(check)):
            if check[i] != target[i]:
                return False
        return True


# Neetcode
# 如果某column的值大於target同位置的值,return False
class Solution:

    def mergeTriplets(self, triplets: List[List[int]],
                      target: List[int]) -> bool:
        good = set()

        for t in triplets:
            # check every value in every rows
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # Ignore the value that is bigger than target...為何不能省略上面兩行？
            # 舉例來說，[[3,5,1],[10,5,7]] => [10, 5, 7][3,5,7]
        #    如果沒有先確認最大值，就會以錯為對了
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
                    # 2/14 不可寫作‘good.add(n)’!!!
                    #      因為good是set,而數字可能重複
        return len(good) == 3


class Solution:

    def mergeTriplets(self, triplets, T):
        forbidden = set()
        for i, [x, y, z] in enumerate(triplets):
            if x > T[0] or y > T[1] or z > T[2]:
                forbidden.add(i)

        a, b, c = 0, 0, 0
        for i, (x, y, z) in enumerate(triplets):
            if i not in forbidden:
                a, b, c = max(a, x), max(b, y), max(c, z)

        return [a, b, c] == T