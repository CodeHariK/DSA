# [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/description/)

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

```py
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            # Check if the current path is a valid IP address
            if start == len(s) and len(path) == 4:
                result.append(".".join(path))
                return

            # Try to form a segment with 1, 2, or 3 digits
            for size in range(1, 4):
                end = start + size
                if end <= len(s):
                    segment = s[start:end]
                    if 0 <= int(segment) <= 255 and (size == 1 or segment[0] != '0'):
                        backtrack(end, path + [segment])

        result = []
        backtrack(0, [])
        return result
```
