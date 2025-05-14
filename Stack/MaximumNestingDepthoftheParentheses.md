# [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses)

```py
class Solution:
    def maxDepth(self, s: str) -> int:
        cnt,max=0,0
        for i in s:
            if i=='(':cnt+=1
            if i==')':cnt-=1
            if cnt>max:
                max=cnt
        return max
