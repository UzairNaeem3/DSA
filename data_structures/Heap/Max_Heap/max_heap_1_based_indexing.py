import sys

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0 
        self.Heap = [None] * (maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
    
    def parent(self, idx):
        return idx // 2       # In 1 based indexing (i) // 2
    
    def leftChild(self, idx):
        return 2 * idx        # In 1 based indexing 2 * i
    
    def rightChild(self, idx):
        return (2 * idx) + 1   # In 1 based indexing (2*i) + 1
    
    def isLeaf(self, idx):     # (size // 2) and i <= size
        if idx >= (self.size // 2) and idx <= self.size:
            return True
        return False
    
    def swap(self, first, second):
        self.Heap[first], self.Heap[second] = self.Heap[second], self.Heap[first]
        
        
    def maxHeapify(self, idx):
        if not self.isLeaf(idx):
            if (self.Heap[idx] < self.Heap[self.leftChild(idx)] or 
                self.Heap[idx] < self.Heap[self.rightChild(idx)]):
                
                if (self.Heap[self.leftChild(idx)] > self.Heap[self.rightChild(idx)]):
                    self.swap(idx, self.leftChild(idx))
                    self.maxHeapify(self.leftChild(idx))
                
                else:
                    self.swap(idx, self.rightChild(idx))
                    self.maxHeapify(self.rightChild(idx))
    
    
    def removeMax(self):
        if self.size <= 0:
            return
        
        elif self.size == 1:
            self.size -= 1
            return self.Heap[self.FRONT]
        
        else:
            root = self.Heap[self.FRONT]
            self.Heap[self.FRONT] = self.Heap[self.size]
            self.size -= 1
            self.maxHeapify(self.FRONT)
            
        return root
    
    
    def insertNode(self, element):
        if self.size >= self.maxsize:
            return
        
        else:
            self.size += 1
            self.Heap[self.size] = element
            
            current = self.size
            while current != 0 and self.Heap[self.parent(current)] < self.Heap[current]:
                self.swap(current, self.parent(current))
                current = self.parent(current)
                
    
    def currentSize(self):
        return self.size
                
                
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print("PARENT NODE : " + str(self.Heap[i]) +
                " LEFT CHILD : " + str(self.Heap[2 * i]) +
                " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
        
        
    
    
if __name__ == "__main__":
    
    maxHeap = MaxHeap(15)
    maxHeap.insertNode(5)
    maxHeap.insertNode(9)
    maxHeap.insertNode(1)
    maxHeap.insertNode(11)
    maxHeap.insertNode(28)
    maxHeap.insertNode(19)
    maxHeap.insertNode(7)
    maxHeap.insertNode(2) 
    maxHeap.insertNode(8)

    maxHeap.Print()
    print()
    print("Current size of the Heap: ",maxHeap.currentSize())
    
    print("The Max val is of Max Heap will be " + str(maxHeap.removeMax()))
    
                     
            
            