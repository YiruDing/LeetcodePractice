# 超快解法
class Solution(object):
def getSum(self, a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    list=[a,b]
    return sum(list)

# the solution that can't pass...
# https://leetcode.com/problems/sum-of-two-integers/discuss/776952/python-best-leetcode-371-explanation-for-python

# https://donic0211.medium.com/leetcode-371-sum-of-two-integers-33fbdefbe71f
# Not so good but workable

# 蠻好的解法
#         1.Why carry is a&b:
#         If a and b are both 1 at the same digit, it creates one carry.
#         Because you can only use 0 and 1 in binary, if you add 1+1 together, it will roll that over to the next digit, and the value will be 0 at this digit.
#         if they are both 0 or only one is 1, it doesn't need to carry.

#         Use ^ operation between a and b to find the different bit
#         In my understanding, using ^ operator is kind of adding a and b together (a+b) but ignore the digit that a and b are both 1,
#         because we already took care of this in step1.	

class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff
        # int(mask) 為4294967295
        # !!重點不是數字!!
        # 10/17JM:因為Ｐython沒有bit限制，無法處理溢位的問題，所以以此限制其為32bit，才不會變成沒完沒了的bit..
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # for overflow condition like
        # -1
        #  1
        return a&mask if b > mask else a
# 類似解法
class Solution:

    def getSum(self, a, b):
        mask = 0xffffffff
        # 一个f代表4个1, 所以就是2进制的32个1. 因为int 为带符号类型，带符号类型最高为是符号位，又因为0xFFFFFFFF，也就是四个字节32 bits全是1, 符号位是1，所以这个数是负数。
        sum = (a ^ b) & mask
        carry = a & b
        while carry != 0:
            a = sum
            b = (carry << 1) & mask
            sum = (a ^ b) & mask
            carry = a & b
            # 0501
            # Why do we need to do it twice?
            # Is there any way not to repeat the code?
        if sum & 0x80000000:
            sum -= 0x100000000
        return sum


# https://leetcode.com/problems/sum-of-two-integers/discuss/84350/Most-Straightforward-Python-Solution!
class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a

        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign.
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a
        
# 10/17 Neetcode更新的答案
# 10/17JM:其實麻煩的是負數...會有無限多“1”加個不停的問題
class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            # 如果兩個都為正比較簡單，一正一負比較麻煩
            # 那如果兩個都是負的呢？
            
            if a > 0:
                return self.getSum(b, a)
            # 交換位置，使第一個parameter為負
            if add(~a, 1) == b:  # -a == b
                return 0
            # 假設兩個相加為零（在bit內須先按位取反，然後加一），就這樣處理
            if add(~a, 1) < b:  # -a < b
                # ~是運算元
                # a的絕對值較大...-a和-b相加，然後取負號
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        return add(a, b)  # a*b >= 0 or (-a) > b > 0
    
#！！！10/3 這個我看得懂！ 但不能直接轉為Python

# https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/371md.html
# JS解
# var getSum = function(a, b) {
#     if(b==0){return a};
#     if(a==0){return b};  

#     while(b!=0){
#         var carry = a&b; //進位值

#         a = a^b;         //相加

#         b = carry << 1;  //進位
#     }
#     return a;
# };