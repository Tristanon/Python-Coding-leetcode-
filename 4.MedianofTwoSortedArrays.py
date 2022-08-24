class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        s1 = nums[len(nums)//2]
        s2 = nums[len(nums)//2 -1]
        T = len(nums)%2
        if T == 0:
            median = (s1 + s2)/2
            return median
        else: 
            median = nums[len(nums)//2]
            return median