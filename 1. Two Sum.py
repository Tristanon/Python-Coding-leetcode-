class Solution(object):
    def twoSum(self, nums, target):
        
        nums: List[int]
        target: int
         List[int]
        
        for i in range(len(nums)):
        	for j in range(i + 1, len(nums)):
        		Tong = nums[i] + nums[j]
        		if Tong == target:
        			return[i,j] 

