class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        quants = {}
        for val in arr:
            if val in quants:
                quants[val] += 1
            else:
                quants[val] = 1
        seen = set()
        for value in quants.values():
            if value in seen:
                return False
            seen.add(value)
        return True