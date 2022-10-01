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
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
