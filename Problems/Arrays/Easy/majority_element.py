def majority_element(nums):
    
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for key, value in freq.items():
        if value > len(nums)/2:
            return key

def majority_element_Boyer_Moore(nums):
    # initialize the candidate and the counter
    candidate = None
    count = 0
    # loop through the array
    for num in nums:
        # if the counter is zero, change the candidate to the current element and set the counter to one
        if count == 0:
            candidate = num
            count = 1
        # otherwise, if the current element is equal to the candidate, increment the counter
        elif num == candidate:
            count += 1
        # otherwise, decrement the counter
        else:
            count -= 1
    # verify that the candidate is a majority element by counting its frequency
    freq = 0
    for num in nums:
        if num == candidate:
            freq += 1
    # if the frequency is more than half of the array size, return the candidate
    if freq > len(nums) // 2:
        return candidate
    # otherwise, return -1 to indicate no majority element exists
    else:
        return -1


if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    print(majority_element(nums))
    print(majority_element_Boyer_Moore(nums))