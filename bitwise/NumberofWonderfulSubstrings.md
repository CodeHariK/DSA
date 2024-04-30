# [1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings)

```py
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024  # Initialize an array to store counts for each bitmask (0 to 2^10 - 1)
        count[0] = 1  # Initially, there's an empty string with no letters appearing an odd number of times
        bitmask = 0  # Initialize bitmask
        result = 0  # Initialize the result
        
        for char in word:
            char_index = ord(char) - ord('a')  # Get the index of the character
            
            # Toggle the bit corresponding to the current character in the bitmask
            bitmask ^= 1 << char_index
            
            # Add the count of substrings with the same bitmask
            result += count[bitmask]
            
            # Add the count of substrings where flipping a single bit gives a wonderful substring
            for i in range(10):
                result += count[bitmask ^ (1 << i)]
            
            # Increment the count for the current bitmask
            count[bitmask] += 1
        
        return result
```
