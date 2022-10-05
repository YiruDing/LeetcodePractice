# https://www.youtube.com/watch?v=UcoN6UjAI64


class Solution:

    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            # Getting the 1st bit from n
            #  & 1
            # To make sure we can process each bit
            result = result | (bit << (31 - i))
            # Updating in a reverse order:
            # since value of result starts with 0 ,we would be able to put each bit on the reserse position
            # June 23 : and store/extend the value one by one
        return result

# 00000010100101000001111010011100
# index: 0
# bit: 0
# result: 0b0
# index: 1
# bit: 0
# result: 0b0
# index: 2
# bit: 1
# result: 0b100000000000000000000000000000
# index: 3
# bit: 1
# result: 0b110000000000000000000000000000
# index: 4
# bit: 1
# result: 0b111000000000000000000000000000
# index: 5
# bit: 0
# result: 0b111000000000000000000000000000
# index: 6
# bit: 0
# result: 0b111000000000000000000000000000
# index: 7
# bit: 1
# result: 0b111001000000000000000000000000
# index: 8
# bit: 0
# result: 0b111001000000000000000000000000
# index: 9
# bit: 1
# result: 0b111001010000000000000000000000
# index: 10
# bit: 1
# result: 0b111001011000000000000000000000
# index: 11
# bit: 1
# result: 0b111001011100000000000000000000
# index: 12
# bit: 1
# result: 0b111001011110000000000000000000
# index: 13
# bit: 0
# result: 0b111001011110000000000000000000
# index: 14
# bit: 0
# result: 0b111001011110000000000000000000
# index: 15
# bit: 0
# result: 0b111001011110000000000000000000
# index: 16
# bit: 0
# result: 0b111001011110000000000000000000
# index: 17
# bit: 0
# result: 0b111001011110000000000000000000
# index: 18
# bit: 1
# result: 0b111001011110000010000000000000
# index: 19
# bit: 0
# result: 0b111001011110000010000000000000
# index: 20
# bit: 1
# result: 0b111001011110000010100000000000
# index: 21
# bit: 0
# result: 0b111001011110000010100000000000
# index: 22
# bit: 0
# result: 0b111001011110000010100000000000
# index: 23
# bit: 1
# result: 0b111001011110000010100100000000
# index: 24
# bit: 0
# result: 0b111001011110000010100100000000
# index: 25
# bit: 1
# result: 0b111001011110000010100101000000
# index: 26
# bit: 0
# result: 0b111001011110000010100101000000
# index: 27
# bit: 0
# result: 0b111001011110000010100101000000
# index: 28
# bit: 0
# result: 0b111001011110000010100101000000
# index: 29
# bit: 0
# result: 0b111001011110000010100101000000
# index: 30
# bit: 0
# result: 0b111001011110000010100101000000
# index: 31
# bit: 0
# result: 0b111001011110000010100101000000
