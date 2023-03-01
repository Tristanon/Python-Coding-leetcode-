# Solution 1:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for index in range(len(nums)):
            if nums[index] != index:  
                return index
        return len(nums)
# Solution 2:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_num = set()
        for num in nums:
            set_num.add(num)

        for index in range(len(nums)):
            if index not in set_num:  
                return index
        return len(nums)