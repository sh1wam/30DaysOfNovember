# nums is an array, target is an integert
# Return the indices of two number that add upto target

# Assume that:
# Each input has exactly one solution
# The same element may not be used twice

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i