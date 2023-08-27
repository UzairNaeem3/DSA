"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

"""
def two_sum(nums, target):
    size = len(nums)
    hash_map = {}
    
    for i in range(size):
        complement = target - nums[i]
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        # Otherwise, store the current element and its index in the hash map
        else:
            hash_map[nums[i]] = i
          
    # if no solution is find, return empty list  
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # output = [0, 1]

