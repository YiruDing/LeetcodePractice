class Solution:

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        def dfs(node):
            # Or you can put(node,curSum)
            if not node:
                return

            nonlocal curSum
            dfs(node.right)
            temp = node.val
            # Store the current value so that you will not add the updated node.val to the next one
            node.val += curSum
            # update the current value
            curSum += temp
            # Prepare for the next one
            dfs(node.left)

        dfs(root)
        return root
