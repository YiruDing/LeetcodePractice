# https://www.youtube.com/watch?v=UcoN6UjAI64

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            bit = (n >> i) & 1
            #  & 1
            # To make sure we can process each bit
            result = result | (bit << (31 - i))
            # since result was 0
            # we would be able to put each bit on the reserse position
        return result
       