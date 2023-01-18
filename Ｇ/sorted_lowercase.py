#  https://leetcode.com/discuss/interview-question/2122202/Google-or-Screening

from heapq import heappush, heappop
from string import ascii_lowercase

class Solution:
    def solve(self, string):
        chars = list(string)
        heap = []

        for char in chars:
            if char in ascii_lowercase:
                heappush(heap, char)
        
        result = [None] * len(string)
        for index, char in enumerate(string):
            if char in ascii_lowercase:
                result[index] = heappop(heap)
            else:
                result[index] = char
        
        return ''.join(result)

print(Solution().solve("Test@123 Google")) #'Output: Teeg@123 Gloost'

# 另解
##Python Time O(N) space O(N)

def sortStr(s):
n = len(s)
res = list(s)

dictS = {}
for i in range(len(s)):
    if s[i].islower():
        if s[i] in dictS:
            dictS[s[i]] += 1
        else:
            dictS[s[i]] = 1

alpha = "abcdefghijklmnopqrstuvwxyz"
for i, c in enumerate(res):
    if c not in dictS:
        continue
    for char in alpha:
        if char in dictS and dictS[char] > 0:
            res[i] = char
            dictS[char] -= 1
            break 
return "".join(res)
