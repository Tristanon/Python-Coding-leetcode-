# 1248.Count_Number_of_Nice_Subarrays.py
# Solution 1:
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        answer = current = 0

        for num in nums:
            current += num%2
            answer += counts[current-k]
            counts[current] +=1
        return answer