class Solution:

    def hammingWeight(self, n: int) -> int:
        # The input would be 32 bit
        result = 0
        while n:
            result += n % 2
            # Or n & 1
            n = n >> 1
            # shift to right by one
        return result


# time and space complexity are both O(1)
# constant time/space

# Another way to only grap "1"


# Another solution:
# Need some more time to figure it out...
class Solution:

    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            # As there are 1 bits...
            n = n & (n - 1)
            # n &= (n-1)
            #  Or you can write
            #  n &= (n-1)
            # Counting the num to exactly 1 bit
            # Skip all the zero in between
            result += 1
        return result
