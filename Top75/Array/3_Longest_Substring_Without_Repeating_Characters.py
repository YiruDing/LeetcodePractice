# Hash Table
# Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        begin=0
        result=0
        
        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[begin])
                begin +=1
            charSet.add(s[end])
            result=max(result,end-begin+1)
        return result
                
# JS solution:
# https://www.youtube.com/watch?v=6vVrHdcodXM

        
        
        