# [48. Rotate Image](https://leetcode.com/problems/rotate-image/description/)

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for y in range(n):
            for x in range(y,n):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        for i in range(n):
            matrix[i].reverse()
```
