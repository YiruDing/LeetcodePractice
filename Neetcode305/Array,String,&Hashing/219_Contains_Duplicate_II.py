class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}

        for i, n in enumerate(nums):
            if n in check and i - check[n] <= k:
                return True
            check[n] = i
        return False