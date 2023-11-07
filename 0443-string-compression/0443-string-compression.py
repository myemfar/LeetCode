class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return []
        result = [chars[0]]
        temp = 0
        for char in chars[1:]:
            if char == result[-1]:
                temp += 1
            elif temp == 0:
                result.append(char)
            else:
                n = str(temp + 1)
                for digit in n:
                    result.append(digit)
                temp = 0
                result.append(char)
        if temp != 0:
            n = str(temp + 1)
            for digit in n:
                result.append(digit)
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)