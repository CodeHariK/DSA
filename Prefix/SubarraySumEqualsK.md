# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret, pre, n = 0, 0, len(nums)
        d = {0: 1}
        for num in nums:
            pre += num
            if pre - k in d:
                ret += d[pre-k]
            d[pre] = d.get(pre, 0) + 1
        return ret
```
