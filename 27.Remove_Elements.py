class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while True:
            if index == len(nums):
                break
            if nums[index] == val:
                nums.remove(nums[index])
            else:
                index +=1