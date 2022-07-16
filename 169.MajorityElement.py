class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target, d = len(nums)/2, {i:0 for i in nums}
        for i in nums:
            if d[i]+1>target:
                return i
            else:
                d[i] += 1