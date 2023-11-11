class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k >= len(nums):
            return sum(nums)/len(nums)
        summed = sum(nums[:k])
        maximum = summed
        for i in range(k, len(nums)):
            summed = summed - nums[i-k] + nums[i]
            maximum = max(maximum, summed)
        return maximum/k