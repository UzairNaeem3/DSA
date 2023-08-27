def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    
    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    running_sum(nums)
    print(nums)  # Output: [1, 3, 6, 10]
