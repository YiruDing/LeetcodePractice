# 10:12
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            # Add 2 lines above !

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                    or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            result = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                      or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))
            # 7:45 the reason of cleaning up (r,c)
            return result

    # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
                # ???不能直接return dfs(r, c, 0)

        return False


# time complexity 較好的解答 11/25未看
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    # 3:42
    def exist(self, board, word):
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True

        return False

    def getWords(self, board, word, i, j, visited, pos=0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(
                board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
            # 2/10 '\' 為續行符號，用來處理過長的code...後面不能加任何東西
                or self.getWords(board, word, i, j - 1, visited, pos + 1) \
                or self.getWords(board, word, i + 1, j, visited, pos + 1) \
                or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res