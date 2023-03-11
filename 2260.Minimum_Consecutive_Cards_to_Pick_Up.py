# 2260.Minimum_Consecutive_Cards_to_Pick_Up.py
# First solution:
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = defaultdict(list)
        for index in range(len(cards)):
            seen[cards[index]].append(index)

        answer = float(inf)
        for key in seen:
            if len(seen[key]) < 2:
                continue
            first = 0
            second = 1
            while second < len(seen[key]):
                answer = min(answer,seen[key][second] - seen[key][first]+1)
                first +=1
                second +=1
        if answer == float(inf):
            return -1
        return answer
            
            