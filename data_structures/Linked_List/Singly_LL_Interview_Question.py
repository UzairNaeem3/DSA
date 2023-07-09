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
            current_node = self.head
            output = ''
            while current_node:
                suffix = ''
                if current_node.next is None:
                    suffix = '-->'
                output += str(current_node.value) + suffix
                current_node = current_node.next
            
            print(output)
            return

if __name__ == "__main__":
    data_list = ["r","e","v","e","r","s","e","d"]
    ll = SpecialLinkedList(data_list)