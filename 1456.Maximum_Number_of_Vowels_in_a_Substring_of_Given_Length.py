# first solution
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters = ['a','e','i','o','u']
        left = total_vowel = 0
        max_vowel = 0
        for right in range(len(s)):
            if s[right] in vowel_letters:
                total_vowel += 1
            while right - left + 1 == k:
                max_vowel = max(max_vowel,total_vowel)
                if s[left] in vowel_letters:
                    total_vowel -= 1
                left +=1
        return max_vowel