class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k >= len(s):
            vowels = 0
            for letter in s:
                if letter in 'aeiou':
                    vowels += 1
            return vowels
        max_vowels = 0
        for letter in s[:k]:
            if letter in 'aeiou':
                max_vowels += 1
        if max_vowels == k:
            return max_vowels
        temp_vowels = max_vowels
        for i in range(k, len(s)):
            if s[i-k] in 'aeiou':
                temp_vowels -= 1
            if s[i] in 'aeiou':
                temp_vowels += 1
            max_vowels = max(max_vowels, temp_vowels)
            if max_vowels == k:
                return max_vowels
        return max_vowels