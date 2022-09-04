class Solution:
    def jump(self, nums: List[int]) -> int:
        Maxjump = 0
        jump = 0
        Curlocation = 0
        for idx, n in enumerate(nums):
            if Curlocation < idx:
                Curlocation = Maxjump
                jump +=1
            if idx  + n  > Maxjump:
                Maxjump = idx + n
        return jump