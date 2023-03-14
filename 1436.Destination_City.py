# 1436.Destination_City.py
# Solution 1:
from collections import defaultdict
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        set_des = set()
        for path in paths:
            set_des.add(path[0])
        for path in paths:
            if path[1] not in set_des:
                return path[1]