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
# Second solution:
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for index in range(1,len(nums)):
            prefix_sum.append(nums[index] + prefix_sum[-1])

        answer = 0
        for index in range(len(nums)-1):
            left = prefix_sum[index]
            right = prefix_sum[-1] - prefix_sum[index]
            if left >= right:
                answer += 1
        return answer 
# Third soulution: avoid calculating all the prefix_sum
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        answer = left_section = 0
        last_prefix_sum = sum(nums)

        for index in range(len(nums)-1):
            left_section += nums[index]
            right_section = last_prefix_sum - left_section
            if left_section >= right_section:
                answer += 1
        return answer 