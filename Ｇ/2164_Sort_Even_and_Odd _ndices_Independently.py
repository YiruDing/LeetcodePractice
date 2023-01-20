def sortEvenOdd(self, A):
    nums[::2] = sorted(nums[::2])
    nums[1::2] = sorted(nums[1::2])[::-1]
    return nums

# 另解
even, odd = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        return [i for t in zip(even, odd) for i in t] + ([even[-1]] if len(even) > len(odd) else [])