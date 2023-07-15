def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursive calls to sort the two halves
    merge_sort(left)
    merge_sort(right)
    
    # Merge the sorted halves
    merge(left,right,arr)

def merge(left,right,arr):
    i = j = 0
    merged_index = 0
    
    # Merge the two sorted arrays
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[merged_index] = left[i]
            i += 1
        else:
            arr[merged_index] = right[j]
            j += 1
        
        merged_index += 1
       
       
    # Merge the sorted halves
    while i<len(left):
        arr[merged_index] = left[i]
        i += 1
        merged_index += 1
    
    while j<len(right):
        arr[merged_index] = right[j]
        j += 1
        merged_index += 1


if __name__ == "__main__":
    arr = [9, 5, 1, 8, 3, 4, 2, 7, 6]
    merge_sort(arr)
    print(arr)
    
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)