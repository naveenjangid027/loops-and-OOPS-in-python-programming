# WAP tp print  the  class & object in python 
#class Student():
#   name = "naveen"
 #   Rollno = 34253
  #  StudentID = 14993

#s1 = Student()
#print(s1.name)
#print(s1.Rollno)
#print(s1.StudentID)


# WAP to class name is Car 
#class Car():
  #  brand = "mercedes"
  # color ="blue"
 #   price = "45.24"

#car1 = Car()
#print(car1.color)
#print(car1.brand)
#print(car1.price)

# Creating Class 
#class Student:
   #  def _init_(self):
 #     print(self)
#      print("adding new student in Database...")
#s1 = Student()
#print(s1)


# WAP to the code 
#class college():
 #def _init_(self,fullname):
  #          self.name = fullname
 #           print("adding the new student Database")
#s1 = college("kana")
#print(s1.name)
#s2 =college("naveen")
#print(s2.name)


# WAP to print
##   college_name = "Vievkananda Institute of Technology "
  #  name = "anoymus" 
 # class attribute 
#def __init__(self,name):
#class Student:
 
 ##      self.name = name  
   #     self.marks = marks 
#
 ##      print("welcome student,", self.name)
   #  
    # def get_marks(self):
     #             return self.marks
      


#s1  = Student("karan",97)
#s1.welcome()
#print(s1.get_marks())

class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def get_avg(self):
            sum = 0
            for val in self.marks:
                sum += val
            print("hi", self.name, "you avg score is:",sum/3)

s1 = Student("tony shark",[97,98,95])
s1.get_avg()