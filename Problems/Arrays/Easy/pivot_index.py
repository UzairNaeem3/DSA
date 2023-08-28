def pivot_index(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    
    left_sum = 0
    
    for i in range(len(nums)):
        # Calculate the right sum by subtracting the current number and the left sum from the total sum
        right_sum = total_sum - nums[i] - left_sum
        
        # if the left sum and the right sum are equal, return the current index
        if left_sum == right_sum:
            return i
        
        # update the left sum by adding the current number
        left_sum += nums[i]
        
    return -1


if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    print(pivot_index(nums))