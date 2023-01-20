# First solution:
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


#Second Solution: 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        add_index = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                nums[add_index] = nums[i+1]
                add_index +=1
        return add_index
test = Solution()
print(test.removeDuplicates([1,1,2,2,3,3]))

# nums = [1,1,2,2,3,3]
# nums[1] = nums[2]
# nums[]
# print(nums)