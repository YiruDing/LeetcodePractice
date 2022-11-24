# NeetCode
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(start, root):
            cur = root
            # ！！dfs的parameter非j和任意字！
            for i in range(start, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        # 11/24: values!!
                        # 可否直接寫cur.children??
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
