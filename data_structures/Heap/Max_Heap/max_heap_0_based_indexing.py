class MaxHeap:
    def __init__(self, max_size):  # Constructor to initialize the MaxHeap object
        self.max_size = max_size
        self.arr = [None] * max_size
        self.heap_size = 0
    
    def heapify(self, idx):  # Heapifies the subtree rooted at idx
        if not self.isLeaf(idx):
            left = self.left_child(idx)
            right = self.right_child(idx)
            largest = idx
            
            if left < self.heap_size and self.arr[left] > self.arr[largest]:
                largest = left
            if right < self.heap_size and self.arr[right] > self.arr[largest]:
                largest = right
            
            if largest != idx:
                self.arr[idx], self.arr[largest] = self.arr[largest], self.arr[idx]
                self.heapify(largest)
    
    def left_child(self, idx):
        return (2*idx + 1)   # In 0 based indexing 2*i + 1

    def right_child(self, idx):
        return (2*idx + 2)   # In 0 based indexing 2*i + 2
    
    def parent(self, idx):
        return (idx-1) // 2  # In 0 based indexing (i-1) // 2
    
    def isLeaf(self, idx):  # (size - 1 // 2) and i < size
        if idx >= (self.heap_size - 1 // 2) and idx < self.heap_size:
            return True
        return False
    
    
    def remove_max(self):    # Removes the maximum element from the heap.
        if self.heap_size <= 0:
            return None
        elif self.heap_size == 1:
            self.heap_size -= 1
            return self.arr[0]
        else:
            root = self.arr[0]
            self.arr[0] = self.arr[self.heap_size-1]
            self.heap_size -= 1
            self.heapify(0)
        
        return root

    def get_max(self):   # Returns the maximum element in the heap
        return self.arr[0]
    
    def current_size(self):  # Returns the current size of the heap
        return self.heap_size
    
    def insert_element(self, element): # Inserts a new element into the max heap
        if self.heap_size == self.max_size:
            print("\nOverflow: Could not insertKey\n")
            return
        else:
            self.heap_size += 1
            idx = self.heap_size - 1
            self.arr[idx] = element
            
            while idx != 0 and self.arr[self.parent(idx)] < self.arr[idx]:
                self.arr[idx], self.arr[self.parent(idx)] = self.arr[self.parent(idx)], self.arr[idx]
                idx = self.parent(idx)
                    
    def remove_element(self, idx): # Deletes the element at the specified index
        if idx >= self.heap_size:
            return None
        else:
            self.arr[idx] = float('inf')
            while idx != 0 and self.arr[self.parent(idx)] < self.arr[idx]:
                self.arr[idx], self.arr[self.parent(idx)] = self.arr[self.parent(idx)], self.arr[idx]
                idx = self.parent(idx)
                
            self.remove_max()
            
    def print_heap(self):  # Prints the elements of the heap
        for item in self.arr[:self.heap_size]:
            print(item, end=" ")
        print()

# Test the max heap
def main():
    max_heap = MaxHeap(5)

    max_heap.insert_element(10)
    max_heap.insert_element(20)
    max_heap.insert_element(30)

    print("Entered 3 elements:- 10, 20, 30")
    print(f"Current size of the heap is {max_heap.current_size()}")
    print("Current maximum element is ", max_heap.get_max())
    max_heap.print_heap()
    print()

    max_heap.remove_element(2)
    print("Deleted element at index 2")
    print(f"Current size of the heap is {max_heap.current_size()}")
    print("Current maximum element is ", max_heap.get_max())
    max_heap.print_heap()
    print()
    
    max_heap.insert_element(20)
    print("Entered element 20")
    print(f"Current size of the heap is {max_heap.current_size()}")
    max_heap.print_heap()
    print()
    
    max_heap.remove_max()
    print("Removed Maximum element which is 30")
    print(f"Current size of the heap is {max_heap.current_size()}")
    max_heap.print_heap()
    
if __name__ == "__main__":
    main()