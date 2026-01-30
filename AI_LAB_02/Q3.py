class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks

        else:
            print("marks should be between 0 & 100")

    def get_marks(self):
        return self.__marks

    def calculate_grade(self):
        if self.__marks > 90:
            return 'A'
        
        if self.__marks > 75:
            return 'B'

        if self.__marks > 65:
            return 'C'

        if self.__marks > 55:
            return 'D'

        return 'F'

student1 = Student(49)
student1.get_marks()
print("grade 1: ", student1.calculate_grade())

student2 = Student(55)
student2.get_marks()
student2.set_marks(78)
print("grade 2: ", student2.calculate_grade())
