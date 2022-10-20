class Solution:

    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
# input 10,[3,5,7],[3,2,1]
# pair: [[3, 3], [5, 2], [7, 1]]
# sorted pair: [[7, 1], [5, 2], [3, 3]]
# stack: [3.0]
# stack: [3.0, 2.5]
# stack: [3.0, 2.3333333333333335]
