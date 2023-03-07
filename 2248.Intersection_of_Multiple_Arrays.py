# First Solution
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        def check(lst1,lst2):
            new_list = []
            set_lst2 = set(lst2)
            for val in lst1:
                if val in set_lst2:
                    new_list.append(val)
            return new_list

        result = nums[0]
        for index in range(1,len(nums)):
            result = check(result,nums[index])
        result.sort()
        return result

        