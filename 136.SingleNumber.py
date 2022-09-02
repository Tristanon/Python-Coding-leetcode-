class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):
            if nums.count(nums[idx]) == 1:
                return nums[idx]
            idx +=1
