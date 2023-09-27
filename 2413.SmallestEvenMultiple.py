class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n == 1:
            return 2
        EvenMultiple = n
        while True:
            if EvenMultiple%2 == 0 and EvenMultiple%n == 0:
                return EvenMultiple
            EvenMultiple += 1
            