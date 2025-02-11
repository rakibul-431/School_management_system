class school:
    def __init__(self,name,addres):
        self.name=name
        self.addres=addres
        self.teachers={}#{"Bangla":Teacher_object}
        self.ClassRooms={}#{"classroom":class_object}
    def add_classroom(self,classroom):
        self.ClassRooms[classroom.name]=classroom
    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher
    def student_admission(self,student):
        classname=student.classroom.name
        self.ClassRooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70 and marks<80:
            return 'A'
        elif marks>=60 and marks<70:
            return 'A-'
        elif marks >=50 and marks<60:
            return 'B'
        elif marks >=40 and marks<50:
            return 'c'
        elif marks >=33 and marks<40:
            return 'D'
        elif marks<33:
            return 'F'
        else:
            print("Invalid marks.")

    @staticmethod
    def grade_to_valu(grad):
        grad_map = {
            'A+':5.00,
            'A' :4.00,
            'A-':3.50,
            'B' :3.00,
            'C' :2.00,
            'D' :1.00
        } 
        return grad_map[grad]   
    @staticmethod
    def valu_to_grade(valu):
        if valu==5.00:
            return 'A+'
        elif valu>=4.00 and valu<5.00:
            return 'A'
        elif valu>=3.5 and valu<4.00:
            return 'A-'
        elif valu>=3.00 and valu<3.5:
            return 'B'
        elif valu>=2.00 and valu<3.00:
            return 'C'
        elif valu >=1.00 and valu<2.00:
            return 'D'
        elif valu >=0.00 and valu<1.00:
            return 'F'
        else:
            print("Invalid input.")
    
    def __repr__(self):
        #All classRoom
        for key,valu in self.ClassRooms.keys():
            print(key)
        #All students
        print("-----------All students--------")
        result=''
        for key,valu in self.ClassRooms.items():
            result+=f'----{key.upper()} ClassRoom student \n'
            for student in valu.student:
                result+=f'student.name\n'
        print(result)
        #All subject
        print("--------All subject----------")
        subject=''
        for key,valu in self.ClassRooms.items():
            subject+=f'----{key.upper()} ClassRoom Subject \n'
            for sub in valu.subject:
                subject+=f'sub.name\n'
        print(subject)
        #All Teachers
        #All students results
        print("--------All student Result---------")
        for key,valu in self.ClassRooms.items():
            for student in valu.students:
                for k,i in student.marks.items():
                    print(student.name ,k,i,student.subject_grade[k])
                print(student.final_grad())
        return ''
