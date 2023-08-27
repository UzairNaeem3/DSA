"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

def moveZeroes(nums):
    n = len(nums)
    non_zero_index = 0  # The index where the next non-zero element should be placed
    
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1
            
    return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(moveZeroes(nums))