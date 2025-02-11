from person import Teacher
from School import school
class subject:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
        self.max_marks=100
        self.pass_marks=33
    def exam(self,students):
        for student in students:
            mark= self.teacher.evaluat_exam()
            student.marks[self.name]=mark
            student.subject_grad[self.name]=school.calculate_grade(mark)

