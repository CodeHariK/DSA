# [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/description/)

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key<root.val:
            root.left = self.deleteNode(root.left,key)
        elif key>root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            curr = root.right
            while curr.left:
                curr=curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right,root.val)
            
        return root
```
