class student:
    def __init__(self,roll_no,name,course):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.__marks=0
        
    def set_marks(self,marks):
        if marks<0 or marks>100:
            print("Invalid marks")
        self.__marks=marks    

    def get_marks(self):
        return self.__marks
    def display(self):
        print("roll no:",self.roll_no)
        print("name:",self.name)
        print("course:",self.course)
        print("marks:",self.__marks)
s1=student(101,"sachin","B.Tech")
s2=student(102,"san","B.Tech")
# s1=student(102,"sachin","B.Tech")
s1.set_marks(90)
print("value fetched through get and set method:",s1.get_marks())
s2.set_marks(80)
print("value fetched through get and set method:",s2.get_marks())
s1.display()          
s2.display()  