# First approach:
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for num in arr:
            if num + 1 in hash_set:
                count +=1
        return count
# Second approach:
class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Do not have to use hashset for this problem
        count = 0
        for num in arr:
            if num + 1 in arr:
                count +=1
        return count
# Third approach:
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        run_length = 1
        for i in range(len(arr)):
            if arr[i - 1] != arr[i]:
                if arr[i - 1] + 1 == arr[i]:
                    count += run_length
                run_length = 0
            run_length += 1
        return count
        
        