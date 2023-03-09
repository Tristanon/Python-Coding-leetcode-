# Ransom_Note.py
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = defaultdict(int)
        count_magazine = defaultdict(int)
        for char in ransomNote:
            count_ransom[char] = count_ransom.get(char,0) + 1
        for char in magazine:
            count_magazine[char] = count_magazine.get(char,0) + 1
        
        for char in count_ransom:
            if count_ransom[char] > count_magazine.get(char,0):
                return False
        return True