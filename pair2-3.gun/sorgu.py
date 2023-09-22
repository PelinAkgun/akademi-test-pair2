from okul_kayit import Student , Teacher
student_list = []
teacher_list = []


def Add(type,object):
    if type == "student":
        student_list.append(object)
    else :
        teacher_list.append(object)
     
student1 = Student("ayse" , 12)
Add("student",student1)
teacher1 = Teacher("ali",3,30)
Add("teacher",teacher1)
def getAll():
    print("ogrenci listesi: ")
    for i in range(len(student_list)):
        print(student_list[i].name , student_list[i].number)
    print("ogretmen listesi : ")
    for l in range(len(teacher_list)):
        print(teacher_list[i].name , teacher_list[i].courses ,teacher_list[i].year)

getAll()