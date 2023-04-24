# 自己解出來了...


class Solution:

    def minSwaps(self, s: str) -> int:
        res = 0
        check = []
        for i in range(len(s)):
            if s[i] == '[':
                check.append(s[i])
            else:
                if len(check) != 0:
                    check.pop()
                else:
                    res += 1
                    # swap 之後，就有‘[’可用了...因為可以為其他‘]’所用，一定要加上去
                    check.append('[')

        return res
# When we did the swap, we took 3 closing brackets and turns into 2 bracket...As we turn 1 of them to be an opening bracket, we would CANCEL OUT 1 of the closing bracket!
# Thus each swap actually gets rid of 2 extra closing brackets