# class members | python objects members
# types of variables 1) class members 2) object members
# class members are shared by all objects of the class
# object members are unique to each object of the class
# class members are accessed by using class name
# object members are accessed by using object name
# class members can be modified by using class name or object name
# object members can be modified by using object name only
# class members are defined inside the class but outside any method
# object members are defined inside the __init__ method of the class
# 1)class members i)declaration: in side the class 
# ii)access:by using class name we can access class members. 
#  iii)modification: by using class name or object name we can modify class members
class section():
    seta=50
    setb=10
ob1=section()
ob2=section()
print('--ACCESSED BY USING CLASS NAME:')
print(section.seta)
print(section.setb)
print('--ACCESSED BY USING OBJECT NAME:')
print(ob1.seta)
print(ob1.setb)
print('--MODIFY BY USING CLASS NAME:')
section.seta=102
section.setb=202
print(ob1.seta)
print(ob1.setb)
print('--MODIFY BY USING OBJECT NAME:')
ob1.seta=127
ob1.setb="hii"
print(ob1.seta)
print(ob1.setb)
# 2)object Members:
#  i)declaration: inside the __init__ method of the class
# ii)access: by using object name we can access object members
# iii)modification: by using object name only we can modify object members
class clg():
    clg_name="bits"
    clg_code="BRNK"
    clg_location="kurnool"
    def __init__(self,student_name,student_id,student_branch):
        self.student_name=student_name
        self.student_id=student_id
        self.student_branch=student_branch
objet=clg("vishnu",590,"cse")
print(objet.student_branch,objet.student_id, objet.student_name, clg.clg_name)
print(f'hi my name is {objet.student_name}, my branch is {objet.student_branch}, from {clg.clg_location}')