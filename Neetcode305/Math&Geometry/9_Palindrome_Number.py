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
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        # 抓到要去頭的除數
        
        while x:
            right = x % 10
            left = x // div
            if right != left:
                return False
            
            x = (x % div) // 10
            # 抓出個位數
            div = div // 100
            #  抓出最大/最左的位數
        return True
