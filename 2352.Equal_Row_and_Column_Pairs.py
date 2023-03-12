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
# Solution 2:
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(array):
            return tuple(array)

        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] +=1

        dic2 = defaultdict(int)
        for index in range(len(grid[0])):
            current_column = []
            for row in grid:
                current_column.append(row[index])
            dic2[convert_to_key(current_column)] +=1
        print(dic)
        print(dic2)
        answer = 0
        for array in dic:
            answer += dic[array] * dic2[array]
        return answer
