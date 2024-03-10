# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

```py
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rotten = deque([(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 2])
        fresh_count = sum(row.count(1) for row in grid)
        minutes = 0

        while rotten and fresh_count:
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        rotten.append((nx, ny))
                        fresh_count -= 1

            minutes += 1

        return minutes if fresh_count == 0 else -1
```
