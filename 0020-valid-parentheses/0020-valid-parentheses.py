class Solution:
    def isValid(self, s: str) -> bool:
        left = '({['
        right = ')}]'
        combined = []
        for char in s:
            if char in left:
                combined.append(char)
            elif char in right:
                if not combined:
                    return False
                if char == ')' and combined[-1] != '(':
                    return False
                if char == ']' and combined[-1] != '[':
                    return False
                if char == '}' and combined[-1] != '{':
                    return False
                combined.pop()
        return len(combined) == 0
        