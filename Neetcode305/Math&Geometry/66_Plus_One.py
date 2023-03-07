# T:O(n) S:O(1)


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                # 3/6 如果到digits尾端，還沒結束的態勢，那就要加一
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1]


# [1,9,9,9]
# digits: [0, 9, 9, 1]
# digits: [0, 0, 9, 1]
# digits: [0, 0, 0, 1]
# digits: [0, 0, 0, 2]