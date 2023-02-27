class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        maxN = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            maxN = max(maxN, arr[i + 1])
            res[i] = maxN
        return res
    
# 另：Neetcode DP
# def replaceElements(self, arr: List[int]) -> List[int]:
    #     rightMax = -1
    #     for i in range(len(arr) -1, -1, -1):
    #         newMax = max(rightMax, arr[i])
    #         arr[i] = rightMax
    #         rightMax = newMax
    #     return arr