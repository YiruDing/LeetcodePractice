# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/1266035/python-very-detailed-explanation-of-one-liner-solution-for-python-beginners/?q=python&orderBy=most_votes
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): 
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False