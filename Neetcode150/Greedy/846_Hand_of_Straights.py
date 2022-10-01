# 10/1 My solution
# To be fixed...
class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) < groupSize:
            return False
        if len(hand) == groupSize:
            return True
        if len(hand) % groupSize:
            return False

        n = len(hand) / groupSize
        newArr = sorted(hand)
        arrangedArr = []
        check = 1
        remainNum = []
        for i in range(len(hand)):
            subArr = []
            while check * (n - 1) <= i < check * n:
                if newArr[i] != newArr[i - 1] + 1:
                    return False

                elif newArr[i] not in subArr:
                    subArr.append(newArr[i])
                else:
                    newArr.append(newArr[i])
#                     怎麼處理重複出現的數字？他們可以屬於不同的group
            check += 1
            newArr = sorted(newArr)

        return True


# Neetcode
class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = collections.Counter(hand)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        # 並非最小值
                        return False
                    heapq.heappop(minH)
                    # 為最小值，所以就可以pop掉，第二小的數字變成最小的
        return True
