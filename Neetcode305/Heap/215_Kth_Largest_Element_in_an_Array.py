# 8/6 哇！我解開了！
# 11/29 minHeap of size K
# 12/6 題目從int改為str所以解答調整了


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nn = [-1 * int(n) for n in nums]
        heapq.heapify(nn)

        while k > 1:
            # 3/10 為何不能用  while len(res) > k:
            # 3/20 JM: 假設1-10 要取第三大的數，理論上是8...但如果用 while 10 > 3去跑，就搞錯了！
            heapq.heappop(nn)
            k -= 1
        return str(-nn[0])


# Neetcode1
# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# Neetcode2
# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]
        # 3/10 這個的indentation要注意

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # https://docs.python.org/3/library/heapq.html
        # heapq.heappush(heap, item)
        # Push the value item onto the heap, maintaining the heap invariant.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)