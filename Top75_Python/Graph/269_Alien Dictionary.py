# Haven't run the code yet...

# Topological sort
# DAG
#在图论中，拓扑排序（Topological Sorting）是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列

#12:22 postOrder DFS BCA

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
                    adj[w1[j]].add([w2[j]])
                    # So we can check the adjacent later
                    break
                
        visit={}
        # F=visited & no longer in the path
        # T=visited & is current path
        result=[]
        
        def dfs(c):
            if c in visit:
                return visit[c]
            # Let's how we detect a loop
            
            visit[c]=True
            for nei in adj[c]:
                if dfs[nei]:
                    return True
            visit[c]=False
            result.append(c)
            # return the result in reverse order later
            
        for c in adj:
            if dfs(c):
                return ""
            # detected a loop
        
        result.reverse()
        return "".join(result)