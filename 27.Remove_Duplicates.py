class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length_of_nums = len(nums) 
        current_index = 0
        test_index = 1
        while True:
            if len(nums) == 1:
                break
            if current_index == len(nums)-1:
                break
            if nums[current_index] == nums[test_index]:
                nums.remove(nums[current_index])
            else:
                if current_index+1 == len(nums) -1:
                    break
                else:
                    current_index +=1
                    test_index +=1 
# e = Solution()
# e.removeDuplicates([1,1,2])
# print(e.removeDuplicates([1,1,2]))
