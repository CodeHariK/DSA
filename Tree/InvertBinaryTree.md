# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)

Given the root of a binary tree, invert the tree, and return its root.

## Py

```py
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = [root]

        while len(ans) != 0:
            f = ans[0]
            if(f):
                c = f.left
                f.left = f.right
                ans.append(f.left)
                f.right = c
                ans.append(f.right)
            ans.pop(0)

        return root
```
