# [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

```py
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, curMax):
            nonlocal count
            if not node:
                return
            if node.val >= curMax:
                count += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        dfs(root, root.val)
        
        return count
```