class Student:
    def __init__(self,name,student_id,email,age,department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,new_email):
        self.__email = new_email

    def display_info (self):
        print(f" name: {self.name} \n Student_id : {self.student_id}\n email: {self.__email}\n Department :{self.department}\n")

    def calculate_result(self,*marks):
        if len(marks)==0:
            return 0
        else :
            total = sum(marks)
            avg = total / len(marks)
            return avg        

    def get_student_type (self):
        return "Regular Student"

#UndergraduateStudent
class UndergraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department,semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    
    def display_info(self):
        super().display_info()
        print(f"Semester:  {self.semester}")

     #overriding
    def get_student_type (self):
        return "UndergraduateStudent"


#GraduateStudent
class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department,research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def display_info(self):
        super().display_info()
        print(f"Research Topic : {self.research_topic}")

    #override
    def get_student_type(self):
        return "GraduateStudent"


print("\n")
#For Under GraduateStudent

UGS = UndergraduateStudent("Adnan","UGS_13","example@b.edu",20,"CSE",11)
UGS.display_info()
print("Type:", UGS.get_student_type())
print("Result:", UGS.calculate_result(80,70,90))
print("Email:", UGS.email)

print("\n")
#For  GraduateStudent

GS = GraduateStudent("Asif","GS_13","exs@b.edu",25,"CSE","Cybersecurity")

GS.display_info()
print("Type:", GS.get_student_type())
print("Result:", GS.calculate_result(60,70,80))
print("Email:", GS.email)

