class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        num = 0
        for el in digits:
            num = num * 10 + el
        return [int(i) for i in str(num + 1)]

        