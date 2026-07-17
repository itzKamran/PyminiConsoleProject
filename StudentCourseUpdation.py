class Student:

   def __init__(self,name,age,roll_no,course,marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.course = course
        self.marks = marks
   def display(self):
       print("Name :",self.name)
       print("Roll :",self.roll_no)
       print("Age :",self.age)
       print("Course :",self.course)
       print("marks :",self.marks)

   def update_mrks(self,new_marks):
       self.marks = new_marks

   def change_course(self,new_course):
       self.course = new_course

student1 = Student("Kamran",101,20,"Bsc.Cs",85)

student1.display()
       
student1.update_mrks(95)
student1.change_course("AI&ml")

print("\n After Update\n")

student1.display()
