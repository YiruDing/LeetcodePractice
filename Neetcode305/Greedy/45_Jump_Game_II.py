# minimum number of jumps.
class Solution:

    def jump(self, nums: List[int]) -> int:
        result = 0
        left = right = 0

        while right < len(nums) - 1:
            # 3/14 記得是len(nums) - 1！
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            result += 1
        return result


# Other solution:
def jump(self, nums):
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    #2/14 r = nums[0]!!
    times = 1
    while r < len(nums) - 1:
        # 2/14 是len(nums) - 1喔，因為我們是要到達The minimum number of jumps to reach the last index
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times
