class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return  # Node already exist
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    
    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):
        left_sum = 0
        right_sum = 0
        if self.left:
            left_sum += self.left.calculate_sum()
        else:
            left_sum = 0
        
        if self.right:
            right_sum += self.right.calculate_sum()
        else:
            right_sum = 0
        
        return left_sum + right_sum + self.data
    
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
            
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        
        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        
        if self.left:
            elements += self.left.pre_order_traversal()
            
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def delete(self, value):
        if self.data is None:
            return "The Binary Search Tree in Empty."
        elif value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
                
        return self
             
                
def build_tree(elements):       
    print("Building tree with these elements:", elements)
    root_node = BinarySearchTreeNode(elements[0])
    print(f"root_node = {elements[0]}")
    
    for i in range(1, len(elements)):
        root_node.add_child(elements[i])
        
    return root_node
        


if __name__ == "__main__":
    
    numbers = [15,12,7,14,27,20,23,88 ]
    numbers_tree = build_tree(numbers)
    
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())