import random
from School import school
class persone:
    def __init__(self,name):
        self.name=name
class Teacher(persone):
    def __init__(self, name):
        super().__init__(name)
    def evaluat_exam(self):
        return random.randint(1,100)
class Student(persone):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom=classroom
        self.__id=None
        self.marks={} #{"Eng":70,"Bangla":65,"math":90}
        self.subject_grad={} #{"Eng":A,"Bangla":A-}
        self.grad=None #Final grade
    def final_grad(self):
        sum=0
        for grad in self.subject_grad.values():
            point=school.grade_to_valu(grad)
            sum+=point
        gpa=sum/len(self.subject_grad)
        self.grad=school.valu_to_grade(gpa)
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def set_id(self,valu):
        self.__id=valu

