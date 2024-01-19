# [931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19)

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

![image](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13

```py
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for y in range(1, n):
            for x in range(0,n):
                matrix[y][x] += min([
                  matrix[y - 1][x-1] if (x > 0) else 999999,
                  matrix[y-1][x],
                  matrix[y - 1][x+1] if (x+1 < n) else 999999,
                ])
        
        return min(matrix[n-1])
```
