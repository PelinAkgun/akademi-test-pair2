class Student :

    def __init__(self , name , number):
        self.name =name
        self.number = number 
    
    def Exam(self ):
         return(f"{self.name} , 2 adet testiniz  bulunmaktadir.")
    
    def Number(self ):
         return(f"{self.name} , numaranız : {self.number}")

class Teacher :
    def __init__(self , name , courses , year):
          self.name = name
          self.courses = courses
          self.year = year
    def CourseCount(self):
         return(f"{self.name} , {self.courses} tane dersiniz bulunmaktadir. ")
    
    def Age(self):
         return(f"{self.name} , {self.year} senedir calismaktasiniz.")

# student1 = Student ("Simge" , 24)
# student1.Exam()
# student1.Number()
# student2 = Student ("Pelin", 23)
# student2.Exam()
# student2.Number()
# student3 =Student ("Ibrahim", 26)
# student3.Exam()
# student3.Number()


# teacher1 = Teacher("Ali" ,3,30)
# teacher1.Age()
# teacher1.CourseCount()
# teacher2 = Teacher("Ayse",5,59)
# teacher2.Age()
# teacher2.CourseCount()
# teacher3 = Teacher("Mahmut" ,13,48)
# teacher3.Age()
# teacher3.CourseCount()
