# https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        a,b = 0,0
        if A and B:
            # 1/26 這個很重要！
            while a < len(A) and b < len(B):
                lo = max(A[a][0],B[b][0])
                hi = min(A[a][1],B[b][1])
                if lo <= hi :
                    res.append([lo,hi])
                if A[a][1] < B[b][1]:
                    a+=1
                else:
                    b+=1
        return res