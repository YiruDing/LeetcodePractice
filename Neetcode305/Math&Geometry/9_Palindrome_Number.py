class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        return x == self.reverseUtil(x)
        
    def reverseUtil(self, x):
        result = 0

        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
            
        return result 
    
# Neetcode
# 技巧：去頭去尾
# 搞不清楚？用13931去跑跑看，就知道了...
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        # 抓到最大位數的除數，來“去頭”(抓出最大/最左的位數)
        
        while x:
            right = x % 10
            left = x // div
            if right != left:
                return False
            
            x = (x % div) // 10
            # 抓出個位數
            div = div // 100
            #  update 最大位數的除數
        return True
