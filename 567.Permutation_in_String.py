# 567.Permutation_in_String.py
# Solution 1:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        def check_permutation(s1, s2):
            if Counter(s1) == Counter(s2):
                return True
            return False

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if check_permutation(s2[left : right + 1], s1):
                return True
            right += 1
            left += 1    
        
        return False
# Solution 2:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, matched = Counter(s1), len(s1), 0   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in cntr: 
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True

        return False