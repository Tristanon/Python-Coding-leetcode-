# Solution 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # create prefix_sum
        prefix_sum = [nums[0]]
        for index in range(1,len(nums)):
            prefix_sum.append(nums[index] + prefix_sum[-1])

        for index in range(len(nums)):
            if index == 0 and prefix_sum[-1] - nums[index] == 0:
                return index 
            elif index > 0 and prefix_sum[index-1] == prefix_sum[-1 ] - prefix_sum[index]:
                return index
        return -1