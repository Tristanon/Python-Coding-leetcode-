class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = current_sum = 0
        answer = len(nums) + 1
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                answer = min(right - left + 1,answer)
                current_sum -= nums[left]
                left += 1
        
        if answer > len(nums):
            return 0
        else:
            return answer