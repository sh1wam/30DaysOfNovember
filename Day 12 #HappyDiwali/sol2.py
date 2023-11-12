class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        return len(set(nums))
        