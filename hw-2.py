class Student:
    def __init__(self, name, student_id, age, gender):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender
    def set_grade(self, grade):
        self.grade = grade
    def get_grade(self):
        return self.grade

    def display_student_info(self):
        print('name: '+self.name)
        print('student_id: '+self.student_id)
        print('age: '+str(self.age))
        if self.gender == 'Female':
            print('gender:Female')
        else:
            print('gender:Male')
        print('Grade:',self.grade) 
            
student1 = Student('Alice', 'A12345', 18, 'Female')
student1.set_grade(45)
student1.display_student_info()