def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        # if swapped flag doesn't change in 1st iteration it means numbers are already sorted       
        if not swapped:    
            break  
    
    
# ! Exercise 
def bubble_sort_string(elements_string, key=None):
    size = len(elements_string)
    
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements_string[j][key]
            b = elements_string[j+1][key]
            if a > b:
                elements_string[j], elements_string[j+1] = elements_string[j+1], elements_string[j]
                swapped = True    
        if not swapped:    
            break  

if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)
    
    elements_string = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    bubble_sort_string(elements_string, key='name')
    print(elements_string)
    
