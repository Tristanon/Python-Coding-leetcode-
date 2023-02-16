# first solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        for index in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[index])
        return prefix_sum