from person import Student,Teacher
from School import school
from Subject import subject
from classRoom import ClassRoom

School=school('ABC','Dhaka')

#Assign class
Eight=ClassRoom('Eight')
Nine=ClassRoom("Nine")
Ten=ClassRoom("Ten")
#Add classroom in school
School.add_classroom(Eight)
School.add_classroom(Nine)
School.add_classroom(Ten)
#Assign student in the class
Tanvir=Student("Tanvir",Eight)
Sujon=Student("Sujon",Nine)
Noyon=Student("Noyon",Ten)
Rakib=Student("Rakib",Ten)
#Admission student
School.student_admission(Tanvir)
School.student_admission(Sujon)
School.student_admission(Noyon)
School.student_admission(Rakib)
#Add Teacher In School
Samat=Teacher("Samat")
Ruben=Teacher("Ruben")
Ashok=Teacher("Ashok")

#adding subject
Bangla=subject("Bangla",Samat)
English=subject("English",Ruben)
Math=subject("Math",Ashok)
physics=subject("physics",Ruben)

Eight.add_subject(Bangla)
Eight.add_subject(English)
Eight.add_subject(Math)

Nine.add_subject(Bangla)
Nine.add_subject(Math)
Nine.add_subject(physics)

Ten.add_subject(English)
Ten.add_subject(Math)
Ten.add_subject(physics)

Eight.take_semeter_final_exam()
print(School)