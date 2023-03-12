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
# My solution;
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        answer = current = left = 0
        seen = set()
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                current +=1
            elif s[right] in seen:
                answer = max(answer,current)
                while True:
                    current -=1
                    seen.remove(s[left])
                    if s[left] == s[right]:
                        seen.add(s[right])
                        current +=1
                        left +=1
                        break
                    left +=1
        return max(answer,current)
            
        