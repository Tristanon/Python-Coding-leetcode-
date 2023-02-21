# Solution 1:
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.arr[i] 
        return sum
