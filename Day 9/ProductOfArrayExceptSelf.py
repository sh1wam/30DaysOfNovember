# Given an integer array, nums,
# return an array, products, such 
# that products[i] is the product of
# all elements of nums except nums[i]

def productExceptSelf(nums):
    length = len(nums)
    products = [1] * length
    for i in range(1, length):
        products[i] = products[i-1] * nums[i-1]

    right = nums[-1]
    for i in range(length-2, -1, -1):
        products[i] *= right
        right *= nums[i]

    return products