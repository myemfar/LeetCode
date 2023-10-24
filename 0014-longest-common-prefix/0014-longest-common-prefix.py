class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = len(strs[0])
        for word in strs[1:]:
            if len(word) < smallest:
                smallest = len(word)
        result = []
        for i in range(smallest):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                result.append(char)
            else:
                break
        return  ''.join(result)

