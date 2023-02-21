# Solution 1:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]
        for index in range(len(gain)):
            answer.append(gain[index] + answer[-1])
        return max(answer)

# Solution 2:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]
        highest_altitude = answer[0]
        for index in range(len(gain)):
            answer.append(gain[index] + answer[-1])
            highest_altitude = max(answer[-1], highest_altitude)
        return highest_altitude