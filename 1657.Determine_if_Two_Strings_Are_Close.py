# 1657.Determine_if_Two_Strings_Are_Close.py
# Solution 1:
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1 = {}
        for char in word1:
            dic1[char] = dic1.get(char,0) + 1
        
        dic2 = {}
        for char in word2:
            dic2[char] = dic2.get(char,0) + 1
        count1 = sorted(dic1.values())
        count2 = sorted(dic2.values())

        set1 = set(word1)
        set2 = set(word2)

        if set1 == set2 and count1 == count2:
            return True
        return False 

