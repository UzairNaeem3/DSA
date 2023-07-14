def insertion_sort(arr):
    size = len(arr)
    
    # Traverse the array starting from the second element
    for i in range(1, size):
        key = arr[i]
        j = i-1
        
        # Shift elements greater than the key to the right
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position
        arr[j+1] = key

if __name__ == "__main__":
    arr = [9, 5, 1, 8, 3, 4, 2, 7, 6]
    insertion_sort(arr)
    print(arr)
    
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')