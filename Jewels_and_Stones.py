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
# Solution 2:
from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for s in jewels:
            for t in stones:
                if s==t:
                    answer +=1
        return answer
# Solution 3: Use Hashset
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)
