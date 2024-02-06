# [133. Clone Graph](https://leetcode.com/problems/clone-graph/description/)

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

```py
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        m = dict()

        t = [node]
        while(t != []):
            m[t[0]] = Node(t[0].val, None)
            for k in t[0].neighbors:
                if(k not in m.keys()):
                    t.append(k)
            t.pop(0)
        for p in m.keys():
            for s in p.neighbors:       
                m[p].neighbors.append(m[s])

        return m[node]

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         hash = {}

#         def dfs(node):
#             if node in hash:
#                 return hash[node]
            
#             copy = Node(node.val)
#             hash[node] = copy
#             for neighbor in node.neighbors:
#                 copy.neighbors.append(dfs(neighbor))
#             return copy
#         if node != None:
#             return dfs(node)
#         else:
#             return None
        
```