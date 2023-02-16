# First solution
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # find the prefix_sum of nums array
        prefix_sum = [nums[0]]
        for index in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[index])
        
        answer = 1
        for index in range(len(prefix_sum)):
            if prefix_sum[index] + answer <= 1:
                answer = 1 - prefix_sum[index]
        return answer