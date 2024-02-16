# [143. Reorder List](https://leetcode.com/problems/reorder-list/)

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

```py
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the linked list into two halves
        second_half = slow.next
        slow.next = None

        # Step 2: Reverse the second half of the linked list
        prev, curr = None, second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev now points to the head of the reversed second half

        # Step 3: Merge the first half and the reversed second half
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        return head
```