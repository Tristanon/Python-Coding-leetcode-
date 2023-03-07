#1941.Check_if_All_Characters_Have_Equal_Number_of_Occurrences.py
# First Solution
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for character in s:
            counts[character] +=1
        occurences = counts[s[0]]
        for character in counts:
            if counts[character] != occurences:
                return False
        return True