# [2997. Minimum Number of Operations to Make Array XOR Equal to K](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k)

```py
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        temp = 0
        for i in nums:
            temp ^= i
        temp ^= k
        return bin(temp).count('1')
```
