class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        max_length = 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1 

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length - 1