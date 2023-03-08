from collections import defaultdict
# 2225.Find_Players_With_Zero_or_One_Losses.py
# Solution 1: Hashset
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        set_zero_lose = set()
        set_one_lose = set()
        set_more_lose = set()
        for winner, loser in matches:
            if (winner not in set_one_lose) and (winner not in set_more_lose):
                set_zero_lose.add(winner)
            if (loser not in set_more_lose) and (loser not in set_one_lose):
                set_one_lose.add(loser)
                if loser in set_zero_lose:
                    set_zero_lose.remove(loser)
            elif (loser in set_one_lose):
                set_one_lose.remove(loser)
                set_more_lose.add(loser)
        return [sorted(list(set_zero_lose)), sorted(list(set_one_lose))] 