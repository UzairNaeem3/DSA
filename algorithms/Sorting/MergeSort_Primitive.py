def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursive calls to sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left,right)

def merge(arr1,arr2):
    merged = []
    i = j = 0
    
    # Merge the two sorted arrays
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
       
       
    # Merge the sorted halves
    while i<len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j<len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


if __name__ == "__main__":
    arr = [9, 5, 1, 8, 3, 4, 2, 7, 6]
    print(merge_sort(arr))