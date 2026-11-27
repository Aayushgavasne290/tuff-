# linkedlist 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None        
    
    def insert(self,data):
        new_node=node(data)
        