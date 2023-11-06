class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x) # convert it to string to avoid negative numbers
        return s == s[::-1] # check if s is equal to reversed s