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
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next        