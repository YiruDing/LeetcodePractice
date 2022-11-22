class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  #pair:[temp,index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([t, i])
        return res
    
    # My adjustment:
    class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  #pair:[index,temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIdx,stackT,  = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([i,t])
        return res