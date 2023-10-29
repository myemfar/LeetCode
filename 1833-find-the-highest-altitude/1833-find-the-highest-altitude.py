class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        highest = 0
        for num in gain:
            height += num
            if height > highest:
                highest = height
        return highest