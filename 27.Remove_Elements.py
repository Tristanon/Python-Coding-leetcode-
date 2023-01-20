# first solution:
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

# second solution:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_index = 0
        change_index = 0
        k = 0
        if len(nums) == 1 and nums[0] != val:
            k = 1
            return k
        while current_index <= len(nums)-1:
            if nums[current_index] != val:
                nums[current_index], nums[change_index] = nums[change_index],nums[current_index]
                change_index +=1
                k +=1
                
            current_index +=1
        return k