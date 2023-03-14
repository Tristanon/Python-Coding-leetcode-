# 1748.Sum_of_Unique_Elements.py
# Solution 1:
from collections import defaultdict
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for num in nums:
            dic[num] = dic.get(num,0) +1
        answer = 0
        for num in dic:
            if dic[num] == 1:
                answer += num
        return answer