# [988. Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf)

```py
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.results = []

        def fun(node, res):

            if node.left:
                fun(node.left, res + chr(97 + node.val))

            if node.right:
                fun(node.right, res + chr(97 + node.val))  


            if not node.left and not node.right:
                res += chr(97 + node.val) 
                self.results.append(res[::-1])        


        fun(root, '')
        self.results.sort()
        return self.results[0]


# class Solution:
#     def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
#         leaf = []
#         root.p = None

#         def dfs(r):
#             if r.left:
#                 r.left.p = r
#                 dfs(r.left)
#             if r.right:
#                 r.right.p = r
#                 dfs(r.right)
#             if not r.left and not r.right:
#                 leaf.append(r)

#         dfs(root)
        
#         ans = ""
#         while leaf and None not in leaf:
#             print([None if a == None else a.val for a in leaf])
#             l = leaf[0]
#             for i in leaf:
#                 if i.val <= l.val:
#                     l = i
#             t = []
#             for i in range(len(leaf)):
#                 if (leaf[i].val <= l.val):
#                     l = leaf[i]
#                     t.append(l)
#                     print(l.val)

#             ans += chr(l.val + ord('a'))

#             print([None if a == None else a.val for a in t])
#             leaf = [a.p for a in t]
#             print([None if a == None else a.val for a in leaf])

#         return ans
```
