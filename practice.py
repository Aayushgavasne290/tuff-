class student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
        
    def display(self):
        print("roll no:",self.roll_no)
        print("name:",self.name)
        
s1=student(101,"sachin")
s1.display()            