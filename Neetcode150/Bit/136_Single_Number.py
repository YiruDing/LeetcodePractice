# n XOR 0 is going to ne n
# duplicate always cancel out
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res=n^res
        return res