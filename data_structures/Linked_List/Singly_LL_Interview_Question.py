class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        

class SpecialLinkedList:
    def __init__(self, arr):
        nodes = [Node(val) for val in arr]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1] 
        self.head = nodes[0]
            
    def __str__(self):
        if self.head is None:
            return "Linked List is empty."
        else:
            current_node = self.head
            output = ''
            while current_node:
                suffix = ''
                if current_node.next:
                    suffix = '-->'  
                output += str(current_node.value) + suffix
                current_node = current_node.next
            return output
        
    def insert(self, root, data):
        new_node = Node(data)
        
        if root is None:
            root = new_node
        else:
            new_node.next = root
            root = new_node
        
        self.head = root
        
        return root, data
    
    def reverse(self, root):
        if root is None or root.next is None:
            return root
        
        previous = None
        current = root
        next = None
        
        while current:
            next = current.next
            current.next = previous
            
            previous = current
            current = next
            
        self.head = previous

if __name__ == "__main__":
    data_list = ["r","e","v","e","r","s","e","d"]
    
    # data_list = [1,2,3]
    ll = SpecialLinkedList(data_list)
    print(ll)
    
    ll.insert(ll.head, 10)
    print(ll)
    
    ll.reverse(ll.head)
    print(ll)
    
    