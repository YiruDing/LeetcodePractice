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
                digits.append(1)
                one = 0
            i += 1
            print("digits:", digits)
        return digits[::-1]


# [1,9,9,9]
# digits: [0, 9, 9, 1]
# digits: [0, 0, 9, 1]
# digits: [0, 0, 0, 1]
# digits: [0, 0, 0, 2]