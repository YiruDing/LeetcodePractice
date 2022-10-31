class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False

                if w1[j] != w2[j]:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
        return True


# 待修
class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def helper(w1, w2):
            for i in range(len(w1)):
                if order[w1[i]] > order[w2[i]]:
                    return False
                elif order[w1[i]] < order[w2[i]]:
                    return True
                else:
                    self.helper(w1[1:], w2[1:])
            return True

            for i in range(len(words)):
                w1 = words[i]
                w2 = word[i + 1] if word[i + 1] else None

                self.helper(w1, w2)