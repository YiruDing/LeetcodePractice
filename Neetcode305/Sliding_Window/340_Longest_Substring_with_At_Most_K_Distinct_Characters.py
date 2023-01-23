class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        start = 0
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
            if len(dic) > k:
                # There are too many distinct letters
                start = min(dic.values()) + 1
                # 重置 minimun index,
                del dic[s[start - 1]]
                # 刪掉讓長度爆表的前一個index
            ans = max(ans, i - start + 1)
        return ans
    
# 另解
class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int: