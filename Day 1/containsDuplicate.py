# Given an integer array nums,
# return True if any value
# appears at least twice in the array,
# return False if every element is distinct

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashet:
                return True
            hashset.add(n)
        return False