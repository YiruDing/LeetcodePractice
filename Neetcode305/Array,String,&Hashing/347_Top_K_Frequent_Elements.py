class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
#2/16 用idx表示出現次數！所以接著可以從後面開始抓進res內
# 長這樣 [[], [3], [2], [1], [], [], []]
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                # !!2/16 記得這個！！
                result.append(n)
                # 長這樣
                # result: [1]
                # result: [1, 2]

                if len(result) == k:
                    # 11/3: Not len(freq)!
                    return result


# 另解
#  快很多
def topKFrequent(self, nums, k):
    c = collections.Counter(nums)
    return heapq.nlargest(k, c, c.get)


# 亦可做   return heapq.nlargest(k, c, key=lambda x:c[x])
# DataFrame.nlargest(n, columns, keep='first')
# https://www.geeksforgeeks.org/python-pandas-dataframe-nlargest/
# heapq.nlargest(n, iterable[, key]) is equivalent to
# sorted(iterable, key=key, reverse=True)[:n] in https://docs.python.org/2/library/heapq.html. Thus, I doubt it is not O(n log k) solution but a O(n log n) solution.