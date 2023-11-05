class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            lvow = False
            rvow = False
            if s[left].lower() in 'aeiou':
                lvow = True
            else:
                left += 1
            if s[right].lower() in 'aeiou':
                rvow = True
            else:
                right -= 1
            if rvow == True and lvow == True:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                lvow = False
                rvow = False
        return ''.join(s)
            
