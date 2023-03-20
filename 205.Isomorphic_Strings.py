# 205.Isomorphic_Strings.py
# Solution 1:
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        n = len(s)
        if len(s) != len(t):
            return False
        for index in range(n):
            if s[index] in dic:
                if dic[s[index]] != t[index]:
                    return False
            elif t[index] in dic.values():
                return False
            else:
                dic[s[index]] = t[index]
        return True