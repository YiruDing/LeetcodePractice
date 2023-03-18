class Solution:

    def canPartition(self, nums):
        t = sum(nums) / 2
        P = set([nums[0]])
        # 因為只要有一個值即可，這樣能省時間
        # 2/13 不是省時間啦！
        # JM:這樣沒法進去for number in list(P)的loop啊！
        for x in nums[1:]:
            for y in list(P):
                # set儲存沒有按照順序喔，iterate應該比較麻煩...
                P.add(x + y)
        # P : {1, 6, 11, 12, 17, 22}
        return t in P
   
    
    # 另解
    # https://leetcode.com/problems/partition-equal-subset-sum/solutions/90628/4-line-passed-python-solution/?q=python&orderBy=most_votes
    class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
            # dictionary.update(iterable)
            # https://www.w3schools.com/python/ref_dictionary_update.asp
        return (sum(nums) / 2.)  in possible_sums  
    
# 3/18 bit的寫法...之後再搞懂
# https://leetcode.com/problems/partition-equal-subset-sum/solutions/276278/python-dp-dfs-memo/

# One way is to treat problem as 0-1 knapsack that we need to pick some of the elements that sum up to target = sum(nums) / 2.
# Suppose dp[i][j] is a boolean that indicates whether we can pick some of the elements from nums[:i+1] to sum up to a specific value s. Thus, if dp[i][j] is True, either dp[i-1][s] is already True(some elements from nums[:i] can already sum up to s), or dp[i-1][s-nums[i]] is True(some elements from nums[:i] plus nums[i] equals to s).
# Therefore, we can have recurrence equation as

# dp[i][j] = dp[i-1][s] or (s >= nums[i] and dp[i-1][s-nums[i]])
# The base case dp[0][0] is True and we can always pick none of elements to sum up to 0.
# And we can use rolling dp arrays to reduce dp size from len(nums) * sum(nums)/2 to sum(nums)/2 since dp[i] depends on dp[i-1] alone.
# The time complexity is O(len(nums) * sum(nums)).

def canPartition(nums):
	s, n = sum(nums), len(nums)
	if s & 1: 
        return False
	s >>= 1
	dp = [True] + [False]*s
	for x in nums:
		dp = [dp[s] or (y >= x and dp[y-x]) for s in range(s+1)]
		if dp[s]: 
            return True
	return False
# And leveraging Python's support for large integer, we can also replace the dp array with a large integer with at most sum(nums)//2 bits. Bit operation is much faster so that we don't even need any pruning.

def canPartition(nums):
    s = sum(nums)
    if s & 1: 
        return False
    s, dp = s // 2, 1
    for x in nums:
        dp |= dp << x
    return dp & 1 << t

# Another solution is DFS + Memoization. We keep trying to reduce nums[j] from target value and see whether target value can be reduced to exactly 0. And with memoization, time complexity can be limited within O(len(nums) * sum(nums)).
# Besides we can iterate from large to small values to prune our DFS:

def canPartition(nums):
	s, n = sum(nums), len(nums)
    memo = {(n,0):True}
    if s & 1: 
        return False
    nums.sort(reverse=True)
    def dfs(i, x):
        if x not in memo:
            memo[i,x] = False
            if x > 0:
                for j in range(i, n):
                    if dfs(j+1, x-nums[j]):
                        memo[i,x] = True
                        break
        return memo[i,x]
    return dfs(0, s >> 1)
# With cache

def canPartition(nums):
	s, n = sum(nums), len(nums)
    memo = {(n,0):True}
    if s & 1: 
        return False
    nums.sort(reverse=True)
    @cache
    def dfs(i, x):
        if x <= 0:
            return x == 0
        for j in range(i, n):
            if dfs(j+1, x-nums[j]):
                return True
        return False
    return dfs(0, s >> 1)

