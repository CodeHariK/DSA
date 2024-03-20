# [1669. Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/description/)

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

```py
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tempA = tempB = list1

        while a>1:
            tempA=tempA.next
            a-=1
        
        while b>=0:
            tempB = tempB.next
            b-=1

        tempA.next = list2
        
        while tempA and tempA.next:
            tempA=tempA.next

        tempA.next = tempB

        return list1
```
