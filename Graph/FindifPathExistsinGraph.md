# [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description)

```py
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         m = defaultdict(list)

#         for i in edges:
#             m[i[0]].append(i[1])
#             m[i[1]].append(i[0])

#         v = []

#         def dfs(s):
#             v.append(s)
#             if s == destination:
#                 return True
            
#             for i in m[s]:
#                 if i not in v and dfs(i):
#                     return True
#             return False

#         return dfs(source)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize a set to keep track of visited nodes
        visited = set()
        
        # Stack for iterative DFS
        stack = [source]
        
        # Iterative BFS
        while stack:
            node = stack.pop()
            visited.add(node)
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return False
```
