# Dutch Nation Flag Problem
# Python program to sort an array with 0, 1 and 2 in a single pass

# By using Pointers
def sort_by_pointers(arr, size):
    
    # Initialize three pointers: low, mid, and high
    low = 0
    mid = 0
    high = size - 1
    
    # Loop until the mid pointer crosses the high pointer
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
    
# By counting approach
def sort_by_counting(arr,size):
    
    # Initialize three counters to count occurrences of 0, 1, and 2 in the array
    count0 = 0; count1 = 0; count2 = 0
    
    # Count the occurrences of 0, 1, and 2 in the array
    for i in range(size):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    
    j = 0
    # Fill the array with '0's based on the count of '0's
    while count0 > 0:
        arr[j] = 0
        j += 1
        count0 -= 1
    # Fill the array with '1's based on the count of '1's
    while count1 > 0:
        arr[j] = 1
        j += 1
        count1 -= 1
    # Fill the array with '2's based on the count of '2's
    while count2 > 0:
        arr[j] = 2
        j += 1
        count2 -= 1    
    
    return arr
    

if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    size = len(arr)
    print(sort_by_pointers(arr, size))
    print(sort_by_counting(arr,size))