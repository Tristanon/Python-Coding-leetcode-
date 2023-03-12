# 2352.Equal_Row_and_Column_Pairs.py
# Solution 1:
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        for index in range(len(grid[0])):
            row = []
            for column in grid:
                row.append(column[index])
            rows.append(row)
        
        count = 0
        for i in range(len(grid[0])):
            for j in range(len(rows[0])):
                if grid[i] == rows[j]:
                    count +=1
        return count