class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # if it already exist...
            cur = cur.children[c]
        cur.isWord = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        result, path = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                    or board[r][c] not in node.children or (r, c) in path):
                return False

            path.add((r, c))
            # Checking (r,c) just like "Word Search", but have to check the kid...
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)
            # Above is to check if theree's a word
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(result)


#  indenttion!!!!
# Turn the set to a list
