# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Go

```Go
    type Key [26]byte

    func strKey(str string) (key Key) {
        for i := range str {
            key[str[i]-'a']++
        }
        return
    }
    func groupAnagrams(strs []string) [][]string {
        groups := make(map[Key][]string)
        for _, v := range strs {
            key := strKey(v)
            groups[key] = append(groups[key], v)
        }
        result := make([][]string, 0, len(groups))
        for _, v := range groups {
            result = append(result, v)
        }
        return result
    }
```

## Java

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);
            
            if (!map.containsKey(sortedWord)) {
                map.put(sortedWord, new ArrayList<>());
            }
            
            map.get(sortedWord).add(word);
        }
        
        return new ArrayList<>(map.values());
    }
}
```

## C++

```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for(auto x: strs){
            string word = x;
            sort(word.begin(), word.end());
            mp[word].push_back(x);
        }
        
        vector<vector<string>> ans;
        for(auto x: mp){
            ans.push_back(x.second);
        }
        return ans;
    }
};
```

## Py

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)
        return d.values()
```
