# 1394.Find_Lucky_Integer_in_an_Array.py
# Solution 1:
from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for num in arr:
            dic[num] = dic.get(num,0) + 1

        answer = -1
        for key in dic:
            if key == dic[key]:
                answer = max(answer,key)
        return answer
