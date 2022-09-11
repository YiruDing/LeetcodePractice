class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            # 如果從0到len(cost)+1，會造成index out of range
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


# [10,15,20]答案是15，因為要爬到index3而非2(value:20)