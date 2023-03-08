# https://www.youtube.com/watch?v=RyBM56RIWrM


class Solution:

    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        offset = 1
        # offset: the most significent bit(1 or 2 or 4 or 8 or 16...) that we have reached so far
        # Dynamic Programing
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            result[i] = 1 + result[i - offset]

        return result


# https://leetcode.com/problems/counting-bits/
def countBits(self, num):
    """
        :type num: int
        :rtype: List[int]
        """

    iniArr = [0]
    if num > 0:
        amountToAdd = 1
        while len(iniArr) < num + 1:
            iniArr.extend([x + 1 for x in iniArr])
    # list1.extend(iterable)
    # 1/2/4/8個為一組，每組會從頭開始，多加1...
    return iniArr[0:num + 1]
