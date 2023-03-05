class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(result[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return result[0]
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
                self.res = 0
                def dfs(r):
                    if not r:
                        return 0
                    left = dfs(r.left)
                    right = dfs(r.right)
                    self.res = max(self.res,  left + right)
                    # 3/5 left + right !

                    return 1 + max(left, right)
                # 3/5 不是 1 + self.res

                dfs(root)
                return self.res
                
                