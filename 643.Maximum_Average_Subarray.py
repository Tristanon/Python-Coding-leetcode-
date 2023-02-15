# First solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = current_average= current_sum = max_average = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while right - left >= k - 1:
                current_average = current_sum / k 
                if current_average <= 0 and left == 0:
                    max_average = current_average
                else:
                    max_average = max(max_average, current_average)
                current_sum -= nums[left]
                left += 1
        return max_average 