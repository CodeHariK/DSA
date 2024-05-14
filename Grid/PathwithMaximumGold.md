# [1219. Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold)

```py
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        visited = set()

        def dfs(i,j):
            if i >= h or j >= w or i < 0 or j < 0 or grid[i][j] == 0 or (i,j) in visited :
                return 0
            visited.add((i,j))
            m = grid[i][j] + max(
                dfs(i-1, j),
                dfs(i+1, j),
                dfs(i, j+1),
                dfs(i, j-1)
            )
            visited.remove((i,j))
            return m

        ans = []

        for i in range(h):
            for j in range(w):
                if (i,j) not in visited and grid[i][j] != 0:
                    ans.append(dfs(i,j))

        return max(ans) if len(ans) != 0 else 0
```
