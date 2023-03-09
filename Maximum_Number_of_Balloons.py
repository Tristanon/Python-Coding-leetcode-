# Maximum_Number_of_Balloons.py
# Solution 1:
from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        word = "balloon"
        for char in word:
            counts[char] = 0
        
        for char in text:
            if char in word:
                counts[char] = counts.get(char,0) + 1
        ans = float(inf)
        ans = min(ans,counts['b'])
        ans = min(ans,counts['a'])
        ans = min(ans,counts['l']//2)
        ans = min(ans,counts['o']//2)
        ans = min(ans,counts['n'])
        return ans