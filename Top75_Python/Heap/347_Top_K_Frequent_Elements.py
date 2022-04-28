# Bucket Sort 5:03


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            # If "n" is not already exist,than "0"
        for n, c in count.items():
            # return the key/value(Here we talk about count) pair
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result