class Solution:
    def romanToInt(self, s: str) -> int:
        def romanInt(letter):
            if letter == 'I':
                return 1
            elif letter == 'V':
                return 5
            elif letter == 'X':
                return 10
            elif letter == 'L':
                return 50
            elif letter == 'C':
                return 100
            elif letter == 'D':
                return 500
            elif letter == 'M':
                return 1000
            else:
                return  0
        solution = 0
        prev_value = 0
        for index, l in enumerate(s[:-1]):
            pointer_value = romanInt(l)
            next_value = romanInt(s[index+1])
            if pointer_value < next_value:
                solution -= pointer_value
            else:
                solution += pointer_value
            prev_value = pointer_value
        solution += romanInt(s[-1])
        return solution

