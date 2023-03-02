class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        checker = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in checker:
                if stack and stack[-1] == checker[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
