# Container With Most Water

[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        s = 0
        l = len(height) - 1

        while s < l:
            hs = height[s]
            hl = height[l]
            m = max(m, min(hs, hl) * (l - s))
            if hs < hl:
                s += 1
            else :
                l -= 1
            
        return m
```
