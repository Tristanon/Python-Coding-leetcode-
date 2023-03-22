# 791.Custom_Sort_String.py
# Solution 1:
from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = defaultdict(int)
        for char in s:
            dic[char] = dic.get(char,0) + 1
        
        current_word = ""
        for char in order:
            if char in s:
                current_word += char*dic[char]
        
        for key in dic:
            if key not in current_word:
                current_word += key*dic[key]
        return current_word