class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        solution = ""
        for i in range(min_length):
            solution += word1[i]
            solution += word2[i]
        if len(word1) > min_length:
            solution += word1[min_length:]
        elif len(word2) > min_length:
            solution += word2[min_length:]
        return solution