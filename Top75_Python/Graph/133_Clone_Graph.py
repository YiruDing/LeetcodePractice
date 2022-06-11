# DFS version
# !! June 9 Make the edges double directed
class Solution:
    def cloneGraph(self, node):
            # def cloneGraph(self, node: 'Node') -> 'Node':
            # "Node" is not defined? 
            
        oldToNew ={}
        
        def clone(node):
            if node in oldToNew:
                # Check if we already made the clone
                return oldToNew[node]
            # If not, let's create the copy
            copy= Node(node.val)
            oldToNew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
                # that's the Node that the list append...
            return copy
        
        return clone(node) if node else None