class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        combined = {}
        for num in nums1:
            if num in nums2:
                combined[num] = 1
        result1 = []
        result2 = []
        for num in nums1:
            if num not in combined and num not in result1:
                result1.append(num)
        for num in nums2:
            if num not in combined and num not in result2:
                result2.append(num)
        return [result1, result2]