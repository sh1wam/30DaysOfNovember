class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m
        for val in nums2:
            nums1[start] = val
            start +=1
        return nums1.sort()