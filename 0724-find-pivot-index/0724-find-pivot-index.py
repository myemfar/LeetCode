class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        ltotal = 0
        for index, num in enumerate(nums):
            total -= num
            if total == ltotal:
                return index
            ltotal += num
        return -1