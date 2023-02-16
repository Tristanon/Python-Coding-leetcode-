# First approach
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = current_length = zero = 0 
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                current_length += 1
            else:
                zero += 1
                current_length +=1
            while zero > k:
                if nums[left] == 0:
                    left += 1
                    zero -= 1
                    current_length -=1
                else: 
                    left += 1
                    current_length -=1
            max_length = max(max_length,current_length)
            
        return max_length
# Second attempt:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1