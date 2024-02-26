# [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/)

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

```py
class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # Check if all timestamps are greater than the target timestamp
        if right == -1:
            return ""

        return values[right][0]
```