class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = len(nums)-1
        left = 0
        current_index = len(nums)-1
        new_list = [0] * len(nums)
        while current_index >= 0:
            if abs(nums[right]) > abs(nums[left]):
                new_list[current_index] = abs(nums[right])
                current_index -=1
                right -=1
            else: 
                new_list[current_index] = abs(nums[left])
                current_index -=1
                left +=1
        return [i * i for i in new_list]