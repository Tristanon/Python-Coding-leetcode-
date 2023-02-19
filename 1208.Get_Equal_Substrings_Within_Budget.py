# first solution
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = current_cost = current_length = 0
        max_length = 0
        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            current_length += 1
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                current_length -= 1
                left += 1
            max_length = max(max_length,current_length)
        return max_length