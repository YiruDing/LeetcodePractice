# https://leetcode.com/problems/longest-nice-subarray/solutions/2527281/java-python-3-sliding-window-bit-manipulation-w-explanation-comments-and-analysis/?orderBy=most_votes
# Algorithm

# Use an integer to represent the set bits within the sliding window; use bitwise OR operation to roll an element into window;
# If there are duplicate set bits in current sliding window, their bitwise AND must be greater than 0; use bitwise XOR to keep rolling the element at left bound out of the sliding window till bitwise AND becomes 0;
# Update the maximum window size.

# bitmask (可翻譯為「位元遮罩)掩码（英語：Mask）在计算机学科及数字逻辑中指的是一串二进制数字，通过与目标数字的按位操作，达到屏蔽指定位而实现需求。


class Solution:

    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        bitmask = 0

        for r in range(len(nums)):
            while bitmask & nums[r]: # nums[r] has duplicate set bits for current sliding window.
                # 如果有相同，開始縮減window
                bitmask = bitmask ^ nums[
                    l]  # remove the corresponding element out of the window.
                l += 1  # shrink left bound of current sliding window.
            #下文：在bit 不同的前提下，持續擴張window
            bitmask = bitmask | nums[r]
            # Expand right bound and put nums[r] into window.
            res = max(res, r - l + 1)  # update the max window size.
        return res