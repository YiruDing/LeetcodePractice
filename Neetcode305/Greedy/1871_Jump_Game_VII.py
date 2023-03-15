class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            # i + minJum 不必加一
            for j in range(start, min(i + maxJump + 1, len(s))):
                # i + maxJump + 1!
                # len(s),不是len(s)-1
                if s[j] == '0':
                    q.append(j)
                    if j == len(s) - 1:
                        # 3/14 這行的indentation要注意！
                        return True
            farthest = i + maxJump
            # 3/14 不是 +=

        return False
        # maxJump = max(1 + maxJump, len(s) - 1)
        # trace1, trace2 = 0, 0

        # def traceToTheEnd(idx, trace1, trace2):
        #     if idx == len(s):
        #         return True
        #     if s[idx + minJump + 1] == '0':
        #         trace1 = idx + minJump + 1
        #     if s[idx + maxJump] == '0':
        #         trace2 = idx + maxJump
        #     if trace1 >= len(s) or trace2 >= len(s):
        #         return True
        #     traceToTheEnd(s[idx + 1:], trace1, trace2)

        # traceToTheEnd(0, trace1, trace2)
        # return False
