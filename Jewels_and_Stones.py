# Jewels_and_Stones.py
# Solution 1:
from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic1 = defaultdict(int)
        for char in jewels:
            dic1[char] += 1
        
        dic2 = defaultdict(int)
        for char in stones:
            dic2[char] += 1
        
        answer = 0
        for char in dic1:
            answer += dic1[char] * dic2[char]
        return answer