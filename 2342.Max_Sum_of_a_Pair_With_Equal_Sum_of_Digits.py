# 2342.Max_Sum_of_a_Pair_With_Equal_Sum_of_Digits.py
# Solution 1:
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_digit = []
        for num in nums:
            string = str(num)
            sum = 0
            for digit in string:
                sum += int(digit)
            sum_digit.append(sum)

        dic = defaultdict(list)
        for index in range(len(sum_digit)):
            dic[sum_digit[index]].append(nums[index])
    
        answer = float(-inf)
        for key in dic:
            if len(dic[key]) > 1:    
                answer = max(answer,dic[key][-1]+dic[key][-2])
            
        if answer == float(-inf):
            return -1
        return answer
            