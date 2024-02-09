# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

```py
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
```