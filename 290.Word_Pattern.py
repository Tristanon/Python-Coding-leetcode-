# 290.Word_Pattern.py
# Solution 1:
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = defaultdict(int)
        n = len(pattern)
        s = s.split()
        if len(pattern) != len(s):
            return False
        for index in range(n):
            if pattern[index] in dic:
                if dic[pattern[index]] != s[index]:
                    return False
            elif s[index] in dic.values():
                return False
            else:
                dic[pattern[index]] = s[index]
        return True