# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Go

```Go
    import "reflect"

    func isAnagram(s string, t string) bool {
        return reflect.DeepEqual(charArr(s), charArr(t))
    }

    func charArr(s string) []int {
        charCount := make([]int,26)
        for _, char := range s {
            charCount[(char - 'a')]++
        }
        return charCount
    }
```

## Java

```java
class Solution {
    public static boolean isAnagram(String s, String t) {
        return Arrays.equals(charArray(s), charArray(t));
    }

    public static int[] charArray(String s) {
        int[] charCount = new int[26];
        for (char c : s.toCharArray()) {
            charCount[c - 'a']++;
        }
        return charCount;
    }
}
```

## C++

```c++
class Solution {
public:
    bool isAnagram(string s, string t) {
        return charArray(s) == charArray(t);
    }

    std::vector<int> charArray(const std::string& s) {
        std::vector<int> charCount(26, 0);
        for (char c : s) {
            charCount[c - 'a']++;
        }
        return charCount;
    }
};
```

## Py

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```
