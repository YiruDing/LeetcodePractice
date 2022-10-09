# Pay attention on how the prefix and postfix are stored in the output array


class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


def productExceptSelf(self, nums):
    """
        :type nums: List[int]
        :rtype: List[int]
        """
    numsLen = len(nums)
    productWithoutSelf = [1] * numsLen

    # productWithoutSelf[i] as product of elements to the left of nums[i].
    for i in range(1, numsLen):
        productWithoutSelf[i] = productWithoutSelf[i - 1] * nums[i - 1]

    # productWithoutSelf[i] multiply product of elements to the right of nums[i].
    rightProduct = 1
    for i in range(numsLen - 1, -1, -1):
        productWithoutSelf[i] *= rightProduct
        rightProduct *= nums[i]

    return productWithoutSelf
