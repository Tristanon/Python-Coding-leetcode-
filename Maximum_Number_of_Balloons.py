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

# Solution 2:
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count, a_count, l_count, o_count, n_count = 0, 0, 0, 0, 0
        for char in text:
            if char == 'b':
                b_count+=1
            elif char == 'a':
                a_count+=1
            elif char == 'l':
                l_count+=1
            elif char == 'o':
                o_count+=1
            elif char =='n':
                n_count+=1
        l_count //=2
        o_count //=2
        return min(b_count, a_count, l_count, o_count, n_count)