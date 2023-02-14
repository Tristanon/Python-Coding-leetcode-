class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = answer = 0
        current_product = 1

        for right in range(len(nums)):
            current_product *= nums[right]
            while current_product >= k:
                current_product //= nums[left]
                left +=1
            answer = answer + right - left +1
        return answer
            