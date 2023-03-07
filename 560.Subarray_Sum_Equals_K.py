# 560.Subarray_Sum_Equals_K.py
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        answer = current_sum = 0 

        for num in nums:
            current_sum += num
            answer += counts[current_sum-k]
            counts[current_sum] += 1
        return answer