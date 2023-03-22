# https://leetcode.com/problems/maximum-length-of-repeated-subarray/solutions/1324248/c-python-dp-kmp-hashing-solutions-clean-concise-o-nlogn/


class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 先n後m
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 外m內n
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans