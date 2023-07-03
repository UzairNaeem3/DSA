class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        else:
            current_node = self.head
            llstr = ''
            while current_node is not None:
                suffix = ''
                if current_node.next is not None:
                    suffix = "-->"
                llstr += str(current_node.data) + suffix
                current_node = current_node.next
        
            print(llstr)
            return
              
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
      
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = Node(data, None)
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
             self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
            
        return count
    
    
    def insert_at(self, index, data):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        current_node = self.head
        while current_node is not None:
            if count == index - 1:
                node = Node(data, current_node.next)
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
            self.head = self.head.next
            return
                
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index - 1:
                if current_node.next is not None:
                    current_node.next = current_node.next.next
                else:
                    current_node.next = None
                break
            
            count += 1
            current_node = current_node.next
            
    def insert_after_value(self, data_after, data_to_insert):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data_after:
                break
            
            current_node = current_node.next
            
        if current_node is None:
            print("Node is not present in Linked List.")
            return
        else:
            node = Node(data_to_insert, current_node.next)
            current_node.next = node
            return
            
    def insert_before_value(self, data_before, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_before:
            self.insert_at_beginning(data_to_insert)
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data_before:
                break
            current_node = current_node.next
            
        if current_node is None:
            print("Node is not present in Linked List.")
            return
        else:
            node = Node(data_to_insert, current_node.next)
            current_node.next = node
 
             
    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return
        
        if data_to_remove == self.head.data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data_to_remove:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
                
            
         
            
            
if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.display()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.display()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.display()
    ll.remove_by_value("figs")
    ll.display()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.display()
    
        
