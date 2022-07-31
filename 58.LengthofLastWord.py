class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        if len(a) == 0:
            return 0
        else:
            return len(a[len(a)-1])

