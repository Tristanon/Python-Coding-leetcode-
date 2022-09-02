class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        jump = nums[0]
        while jump > 0 and idx < len(nums)-1:
            jump -=1
            idx = idx + 1
            if nums[idx] > jump:
                jump = nums[idx]
        if idx == len(nums) - 1:
            return True
        else:
            return False