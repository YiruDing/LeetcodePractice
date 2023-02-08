# 第一試
# Time 和 Space 都是Ｏ（a+b）

# 第二試
# 1.Unilize the original string
# 2.Use the 2 pointer technique
# 3. Start from the end od the string

# Use stack to avoid string modification.
# Time O(N) and space O(N).

def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])
    
# O(1) Space
def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")