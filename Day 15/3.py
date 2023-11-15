class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        if val in nums:
            for i, num in enumerate(nums):
                if num == val:
                    count += 1
                    nums[i] = -1
            nums.sort(reverse=True)

        return len(nums) - count