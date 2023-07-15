def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    
    while gap > 0:
        for i in range(gap, size):
            key = arr[i]
            j = i
            while  arr[j-gap] > key and j>=gap:
                arr[j] = arr[j-gap]
                j -= gap
                
            arr[j] = key 
        
        gap = gap // 2



if __name__ == "__main__":
    arr = [9, 5, 1, 8, 3, 4, 2, 7, 6]
    shell_sort(arr)
    print(arr)
    
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        shell_sort(arr)
        print(arr)