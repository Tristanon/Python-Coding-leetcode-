class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        j = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count +=1
        for j in range(count):
	        nums.remove(0)
	        nums.append(0)
        return nums