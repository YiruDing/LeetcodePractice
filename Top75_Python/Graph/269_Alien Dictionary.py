# Topological sort
# DAG
#在图论中，拓扑排序（Topological Sorting）是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列

#12:22 postOrder DFS BCA


#A passed yet confusing solution to me...
# 看下面的其他解法吧！
class Solution:

    def alienOrder(self, words):
        adj = {c: set() for w in words for c in w}
        # get every character from the word in the "words"

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                # Which means we have invalid order
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    # So we can check the adjacent later
                    break

        visit = {}
        # F=visited & no longer in the current path
        # T=visited & is current path
        result = []

        # To be joined latergit

        #   POSTORDER DFS(BCA)
        def dfs(c):
            if c in visit:
                return visit[c]
            # Let's how we detect a loop

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    # Loop!
                    return True
            visit[c] = False
            result.append(c)
            # return the result in reverse order later

        for c in adj:
            if dfs(c):
                return ""
            # detected a loop

        result.reverse()
        return "".join(result)


#8/22 Input：["wrt","wrf","er","ett","rftt"]中，最後一行為何f在t前？因為每個字不需要排序，是字跟字之間才會排序...一字中的字母要怎麼排，本來就不受限

# Approach 1: Breadth-First Search
# Part 1: Extracting Information
# Part 2: Representing the Relations
# Part 3: Assembling a Valid Ordering

from collections import defaultdict, Counter, deque


def alienOrder(self, words: List[str]) -> str:

    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})

    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                    # 區分出有/無相鄰字母的字，並計算其數目
                break
        else:  # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): return ""

    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    # 先放入無相鄰的字母w
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            # 處理完一個相鄰的字，可以減去其數目
            if in_degree[d] == 0:
                # 沒有相鄰字要處理了，就可以加入queue中
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)


# DFS solution Ｔime complexity好很多...
#9/3 還看不懂...
class Solution:

    def alienOrder(self, words: List[str]) -> str:
        # build the list
        adj_list = {c: [] for word in words for c in word}
        # Step 1: Find all edges and put them in adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    adj_list[d].append(c)
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # {w:[e],r:[t],t:[f],f:[],e:[r]}
        seen, cycle = set(), set()
        output = []

        def dfs(node):
            if node in cycle:
                # e.g.[a:"b",b:"c",c:"a"]
                # 9/5ＪＭ：因為recursion,cycle會一直加下去，直到遇到Ｆalse才會triger上一個return False,一路傳到底
                # 練習print出來！
                return False
            if node in seen:  # no issue no need to visit again , we visit node more then once
                return True

            cycle.add(node)
            for per in adj_list[node]:
                if dfs(per) == False:  # return result
                    # 一但呼叫了dfs(per)，在沒有cycle的前提下，fn會一直跑，這幾個set/dict會一直加
                    return False
            cycle.remove(node)
            seen.add(node)
            output.append(node)

        for c in adj_list:
            if dfs(c) == False:  # found a cycle
                return ""
        return "".join(output)
