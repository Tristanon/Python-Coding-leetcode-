# First solution:
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # find the prefix_sum of nums
        prefix_sum = [nums[0]]
        for index in range(1,len(nums)):
            prefix_sum.append(nums[index] + prefix_sum[-1])
        
        answer = 0 
        for index in range(len(nums)-1):
            if prefix_sum[index] >= prefix_sum[len(nums)-1] - prefix_sum[index+1] + nums[index + 1]:
                answer +=1

        return answer
