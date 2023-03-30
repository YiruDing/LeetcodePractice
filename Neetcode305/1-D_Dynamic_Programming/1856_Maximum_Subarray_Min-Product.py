# JM: 下面這個寫法比較清楚
class Solution:

    def maxSumMinProduct(self, nums: List[int]) -> int:
        n, ans, mod = len(nums), 0, 10**9 + 7

        lft, st = [0], [[nums[0], 0]]  #how many valid numbers on its left
        for i in range(1, n):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append([nums[i], cur])
            lft.append(cur)

        rgt, st = [0], [[nums[-1], 0]]  #how many valid numbers on its right
        for i in range(n - 2, -1, -1):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append(([nums[i], cur]))
            rgt.append(cur)
        rgt.reverse()

        sums, cur = [0], 0  # presum array
        for i in range(n):
            cur += nums[i]
            sums.append(cur)

        for i in range(n):
            ans = max(ans, nums[i] * (sums[i + rgt[i] + 1] - sums[i - lft[i]]))

        return ans % mod


# Leetcode hint:
# Can we find the maximum min-product for every value in the array?

# Monotonic Increasing Stack
# https://ch-hsieh.blogspot.com/2012/12/0.html


# 找某個subaray,找出其“最小值”乘以“整個subarray的和“的最大值
# Consider if EACH VALUE was the minimun value of subarray, then SPREAD OUTWARD
class Solution:

    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stack = []
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
            # prefix[-1]: the last value added in the prefixed array
        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, val * total)
                # 往前一個(或多個)位數，以前一個值去乘自己，看看這個值是否足以取代目前的res
                newStart = start
                # 3/20 為何可以重新設定index?不是應該處理連續的數字？

            stack.append((newStart, n))

        # 從每個位數出發，嘗試所有鄰近的可能後，再從頭開始掃描一次，看有沒有其他可能
        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, val * total)

        return res % (10**9 + 7)