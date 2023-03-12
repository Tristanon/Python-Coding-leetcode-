# Longest_Substring_Without_Repeating_Characters.py
# Given solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        biggest_range = 1
        start_index = 0
        for i in range(1,len(s)):
            if s[i] in s[start_index:i]:
                start_index = s[start_index:i].index(s[i]) + start_index +  1
            if biggest_range < i - start_index + 1:
                biggest_range = i - start_index + 1
        return biggest_range
            
        