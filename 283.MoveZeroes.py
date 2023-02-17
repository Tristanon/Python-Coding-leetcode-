-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Solution 2(better)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        return nums
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right +=1
                left +=1
            else:
                right +=1
        return nums

