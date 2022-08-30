class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Maxsum = nums[0]
        cursum = 0
        for i in nums:
            if cursum < 0:
                cursum = 0
            cursum = cursum + i
            if cursum > Maxsum:
                Maxsum = cursum
        return Maxsum