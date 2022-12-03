# 8/21 先想辦法看懂
# 按照順序去訪察，但為了能到達每個點，順序可調整
class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {u: collections.deque() for u, v in tickets}
        res = ["JFK"]

        tickets.sort()
        for u, v in tickets:
            adj[u].append(v)

        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                # the cur does not have any outgoing places
                return False

            temp = list(adj[cur])
            # Create a copy of adj[cur]
            for v in temp:
                adj[cur].popleft()
                res.append(v)
                # Backtrack
                if dfs(v):
                    return res
                # If it does not return True,we have to backtrack this decision
                res.pop()
                # pop the result
                adj[cur].append(v)
                # Put it back and try again
                # c.f. list.insert(i, elem)
                # The only difference between append() and insert() is that insert function allows us to add a specific element at a specified index of the list unlike append() where we can add the element only at end of the list.
            return False

        dfs("JFK")
        return res
