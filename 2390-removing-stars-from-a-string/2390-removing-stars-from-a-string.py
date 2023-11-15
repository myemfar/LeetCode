class Solution:
    def removeStars(self, s: str) -> str:
        word = list(s)
        stack = []
        
        for char in word:
            if char == '*':
                if stack and stack[-1].isalpha():
                    stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)