# 1512.Number_of_Good_Pairs.py
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        size = len(nums)
        good_pair = 0
        for i in range(size):
            for j in range(i+1,size):
                if nums[i] == nums[j]:
                    good_pair +=1
        return good_pair