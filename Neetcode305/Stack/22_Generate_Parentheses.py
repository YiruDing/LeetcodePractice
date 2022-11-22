class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # Only add open paranthesis if open < n
        # only add a closing parathesis if closed < open
        # valif if open==closed==n
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                s = "".join(stack)
                print("stack:", s)
                res.append(s)
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                print('open:', stack)
                stack.pop()
                # After the backtrack returns,
                # we have to UPDATE the stack(a global varieble. so we have to pop the character that we just add)
                # 10/19 We are not pass it to every single call

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                print('close:', stack)
                stack.pop()

        backtrack(0, 0)
        return res

# 10/19問題：為什麼prin出來，竟然是先close而非open??

# n=3
# stack: ((()))
# close: ['(', '(', '(', ')', ')', ')']
#整個添加完了，才pop掉....下同
# close: ['(', '(', '(', ')', ')']
# close: ['(', '(', '(', ')']
# open: ['(', '(', '(']
#整個添加完了，才pop掉....下面從'（','（'開始

# stack: (()())
# close: ['(', '(', ')', '(', ')', ')']
# close: ['(', '(', ')', '(', ')']
# open: ['(', '(', ')', '(']
#整個添加完了，才pop掉....下面從'（','（',')'開始

# stack: (())()
# close: ['(', '(', ')', ')', '(', ')']
# open: ['(', '(', ')', ')', '(']
# close: ['(', '(', ')', ')']
# close: ['(', '(', ')']
# open: ['(', '(']
#整個添加完了，才pop掉....下面從'（'開始

# stack: ()(())
# close: ['(', ')', '(', '(', ')', ')']
# close: ['(', ')', '(', '(', ')']
# open: ['(', ')', '(', '(']

#下面從'(', ')', '('開始

# stack: ()()()
# close: ['(', ')', '(', ')', '(', ')']
# open: ['(', ')', '(', ')', '(']
# close: ['(', ')', '(', ')']
# open: ['(', ')', '(']
# close: ['(', ')']
# open: ['(']
#pop完就沒有了