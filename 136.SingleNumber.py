-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#First solution
#Bad solution
# em sử dụng hàm .count thử ạ, nhưng để em đổi liền
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):
            if nums.count(nums[idx]) == 1:
                return nums[idx]
            idx +=1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#second solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = nums[0]
        length = len(nums)
        for i in range(1,length):
            r = r^nums[i]
        return r
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
