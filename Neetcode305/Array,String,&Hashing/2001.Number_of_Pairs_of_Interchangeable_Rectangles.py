class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = {}
        res = 0

        for w, h in rectangles:
            ratio[w / h] = 1 + ratio.get(w / h, 0)
        
        for c in ratio.values():
            # 算出所有組合的可能
            if c > 0:
                res += (c * (c - 1)) // 2
                # 有c種選擇，那除了自己之外，就還有c - 1個可以調換的對象..去除重複的，所以要除以二
        
        return res