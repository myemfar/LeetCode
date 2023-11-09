class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if len(s) == 0:
            return True
        for letter in t:
            if (idx > len(s)-1):
                return True
            if letter == s[idx]:
                idx += 1
        return (idx > len(s)-1)