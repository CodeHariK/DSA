# [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree)

```py
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Perform in-order traversal to get a sorted list of values
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        sorted_values = in_order_traversal(root)
        
        # Step 2: Build a balanced BST from the sorted list of values
        def build_balanced_bst(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = build_balanced_bst(values[:mid])
            root.right = build_balanced_bst(values[mid+1:])
            return root
        
        return build_balanced_bst(sorted_values)
```
