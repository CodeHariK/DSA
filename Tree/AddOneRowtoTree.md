# [623. Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree)

```py
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val = val, left = root, right = None)
        
        def dfs(n,c):
            if depth == c + 1:
                p = TreeNode(val=val, left=n.left, right=None)
                n.left = p

                p = TreeNode(val=val, left=None, right=n.right)
                n.right = p

                return root

            if n.left:
                dfs(n.left, c + 1)
            if n.right:
                dfs(n.right, c + 1)

        dfs(root, 1)

        return root
```
