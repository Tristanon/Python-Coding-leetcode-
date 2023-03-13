# Last Solution:
class Solution(object):
    def containsDuplicate(self, nums):
	nums = [1,1,1,3,3,4,3,2,4,2]
	numSet = list(set(nums))
	return numSet
# Practice again:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(nums) == len(set_nums):
            return False
        return True
