def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        
        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
            
    return -1 


def binary_search_recursive(numbers_list, number_to_find, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(numbers_list) - 1
    
    if left_index > right_index:
        return -1    # Number not found
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]
    
    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)
    

if __name__ == "__main__":
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 19
    
    # index = binary_search(numbers_list, number_to_find)
    # print(f"Number found at index {index} using Binary Search.")
    
    # index = binary_search_recursive(numbers_list, number_to_find)
    # print(f"Number found at index {index} using Binary Recursive Search.")
    
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurances(numbers_list, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
    