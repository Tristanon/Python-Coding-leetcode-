# Solution 1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]
        for index in range(len(gain)):
            answer.append(gain[index] + answer[-1])
        return max(answer)