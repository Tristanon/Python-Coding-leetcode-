# 1695.Maximum_Erasure_Value.py
# Solution 1:
from collections import OrderedDict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        current_subarray = OrderedDict()
        current_sum = max_sum = 0
        for num in nums:
            if num not in current_subarray:
                current_subarray[num] = 1
                current_sum += num
            else:
                max_sum = max(current_sum,max_sum)
                while True:
                    popped_element = current_subarray.popitem(False)
                    if popped_element[0] != num:
                        current_sum -= popped_element[0]
                    else:
                        current_subarray[num] = 0
                        break
        return max(max_sum,current_sum)