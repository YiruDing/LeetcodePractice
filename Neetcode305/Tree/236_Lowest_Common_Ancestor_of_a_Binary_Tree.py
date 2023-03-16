# https://www.youtube.com/watch?v=WO1tfq2sbsI
# T:O(N)
# S:O(1) if not counting recursive stack frames, otherwise O(N)
def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    else:
        return l or r


def lowestCommonAncestor(self, root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q


# StefanPochmann...越解越迷糊＠＿＿＠
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right


# Or using that None is considered smaller than any node:


def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    subs = [
        self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right)
    ]
    return root if all(subs) else max(subs)