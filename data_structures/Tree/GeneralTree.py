class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)     
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
            
        return level 
        
    def print_tree(self):
        spaces = "  " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
class Tree:
    def __init__(self, root):       
        self.root = root
        
if __name__ == "__main__":
    
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Vivo"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    tree = Tree(root)
    tree.root.print_tree()
    
    
    
