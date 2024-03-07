# [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= cols or j < 0 or j >= rows or grid[j][i] == 0:
                return 0
            grid[j][i] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        ans = 0
        for j in range(rows):
            for i in range(cols):
                if grid[j][i] == 1:
                    ans = max(ans, dfs(i, j))

        return ans
```
