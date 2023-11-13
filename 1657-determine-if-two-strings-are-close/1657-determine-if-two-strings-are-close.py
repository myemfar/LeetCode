class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        def count_characters(word):
            char_count = {}
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
            return char_count
        freq1 = count_characters(word1)
        freq2 = count_characters(word2)
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        return sorted(freq1.values()) == sorted(freq2.values())