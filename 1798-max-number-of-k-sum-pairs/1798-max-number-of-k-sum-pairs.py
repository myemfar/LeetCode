class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        num_freq = {}
        for num in nums:
            complement = k-num
            if complement in num_freq and num_freq[complement] > 0:
                operations += 1
                num_freq[complement] -=1
            else:
                num_freq[num] = num_freq.get(num, 0) + 1
        return operations