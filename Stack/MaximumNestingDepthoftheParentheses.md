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

# class Solution:
#     def maxDepth(self, s: str) -> int:
#         c = 0
#         ss = ""
#         for i in s:
#             if i == "(" or i == ")":
#                 ss += i
#         while ss != "":
#             c += 1
#             ss = ss.replace("()", "")

#         return c
```
