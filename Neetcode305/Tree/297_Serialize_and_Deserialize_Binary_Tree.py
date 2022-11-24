# similar: String 271(659)

# Use preOrder....How to determine whtere the left tree stop?
# if left == null,than go to the right till it's null
# Then go to the right of the root...


class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
            # Base case
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        vals = data.split(",")
        self.index = 0

        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
