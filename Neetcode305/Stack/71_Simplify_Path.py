# To deal with the double dot, we ganna use pop function in stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ''
        
        for c in path + '/':
            
            if c == '/':
                # 每次遇到‘/’就要盤點一次cur
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += c
                # 這裡有包括sigle dot喔！收進來是要確認是否會累積為double dot
        return '/' + '/'.join(stack)