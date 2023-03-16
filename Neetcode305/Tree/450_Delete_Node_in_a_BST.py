# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:
        if not root: return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            # 置換root.left,但萬一要刪除的就是root.left本人，還是要能銜接其他node...所以必須這樣寫
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # 如果不符合以下特質，就必須處理child(ren) node的問題...假設我們取key值.right取代本來的位置，左右都要調整，而且還要刪除重複的...下面就是在做這樣的事
            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            # 不可省略這行，因為我們要先置換root的值（cur.val），再刪掉重複出現的的cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root