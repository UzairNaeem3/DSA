class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def print_forward(self):
        if self.head is None:
            print("Double linked list is empty.")
            return
        else:
            current_node = self.head
            dllstr = ''
            while current_node is not None:
                suffix = '' 
                if current_node.next is not None:
                    suffix += "-->"
                dllstr += str(current_node.data) + suffix
                current_node = current_node.next
            print(dllstr)
            return
        
    def get_last_node(self):
        if self.head is None:
            print("Double linked list is empty.")
            return
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            return last_node
    
    def print_backward(self):
        if self.head is None:
            print("Double linked list is empty.")
            return
        else:
            last_node = self.get_last_node()
            dllstr = ''
            current_node = last_node
            while current_node is not None:
                suffix = '' 
                if current_node.prev is not None:
                    suffix += "-->"
                dllstr += str(current_node.data) + suffix
                current_node = current_node.prev
            print("Link list in reverse: ", dllstr)
            return
        
    def get_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
            
        return count
    
    def insert_at_beginning(self, data):
        if self.head is None:  
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            
            node = Node(data, None, current_node)
            current_node.next = node
            
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        current_node = self.head
        while current_node is not None:
            if count == index - 1:
                node = Node(data, current_node.next, current_node)
                if current_node.next is not None:
                    current_node.next.prev = node
                current_node.next = node
                break
            
            current_node = current_node.next
            count += 1
            
    def remove_at(self, index):
        if self.head is None:
            return
        
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return
        
        count = 0
        current_node = self.head
        while current_node is not None:
            if count == index:
                if current_node.next is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    current_node.prev.next = None
                break
            
            current_node = current_node.next
            count += 1
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
            
if __name__ == "__main__":
    ll = DoubleLinkedList()
    ll.print_backward()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.print_forward()  
    ll.print_backward()  
    ll.remove_at(2)
    ll.print_forward()  