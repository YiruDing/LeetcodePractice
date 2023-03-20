# Neetcode
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        
        if root1.val != root2.val:
            return False
        
        a = self.flipEquiv(root1.left, root2.left) and self. flipEquiv(root1.right, root2.right)
        b = self.flipEquiv(root1.left, root2.right) and self. flipEquiv(root1.right, root2.left)

        return a or b
    
# 以下二解,出自此網頁
# https://leetcode.com/problems/flip-equivalent-binary-trees/solutions/200514/java-python-3-dfs-3-liners-and-bfs-with-explanation-time-space-o-n/?orderBy=most_votes 
# Iterative version: BFS
def flipEquiv(self, r1: TreeNode, r2: TreeNode) -> bool:
        dq1, dq2 = map(collections.deque, ([r1], [r2]))
        while dq1 and dq2:
            node1, node2 = dq1.popleft(), dq2.popleft()
            if node1 == node2 == None: continue 
            elif not node1 or not node2 or node1.val != node2.val: return False

            if node1.left == node2.left == None or node1.left and node2.left and node1.left.val ==  node2.left.val:
                dq1.extend([node1.left, node1.right])
            else:
                dq1.extend([node1.right, node1.left])
            dq2.extend([node2.left, node2.right])
        return not dq1 and not dq2
    
# Iterative version: DFS
 def flipEquiv(self, r1: TreeNode, r2: TreeNode) -> bool:
        stk1, stk2 = [r1], [r2]
        while stk1 and stk2:
            node1, node2 = stk1.pop(), stk2.pop()
            if node1 == node2 == None: continue 
            elif not node1 or not node2 or node1.val != node2.val: return False
            
            if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
                stk1.extend([node1.left, node1.right])
            else:
                stk1.extend([node1.right, node1.left])
            stk2.extend([node2.left, node2.right])
        return not stk1 and not stk2