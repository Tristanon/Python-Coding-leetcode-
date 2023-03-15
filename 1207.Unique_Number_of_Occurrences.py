# 1207.Unique_Number_of_Occurrences.py
# Solution 1:
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        for num in arr:
            dic[num] = dic.get(num,0) + 1

        dic2 = defaultdict(int)
        for num in dic:
            dic2[dic[num]] +=1
        for num in dic2:
            if dic2[num] > 1:
                return False
        return True