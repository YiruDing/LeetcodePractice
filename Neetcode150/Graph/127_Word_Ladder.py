class Solution:

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                # Find every possible patterns
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        # Start wit the beginWord
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # If it's not the endWord, we are going to take its neighbor(s) and add to the q
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
