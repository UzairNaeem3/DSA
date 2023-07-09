class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        

class SpecialLinkedList:
    def __init__(self, arr):
        root_node = Node(arr[0])
        self.head = root_node
        
        
        current_node = self.head
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            current_node.next = new_node
            current_node = new_node
            
    def printLL(self, root):
        if root is None:
            return "Linked List is empty."
        else:
            current_node = root
            output = ''
            while current_node:
                suffix = ''
                if current_node.next:
                    suffix = '-->'  
                output += str(current_node.value) + suffix
                current_node = current_node.next
            
            print(output)
            return
        
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
    ll = SpecialLinkedList(data_list)
    ll.printLL(ll.head)
    
    ll.insert(ll.head, 10)
    ll.printLL(ll.head)
    
    ll.reverse(ll.head)
    ll.printLL(ll.head)