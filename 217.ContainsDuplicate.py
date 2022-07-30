class Solution(object):
    def containsDuplicate(self, nums):
	nums = [1,1,1,3,3,4,3,2,4,2]
	numSet = list(set(nums))
	return numSet
