# multi level 
class A:
    x=30
class B(A):
    pass
class C(B):
    pass
ob=C()
print(ob.x)
# multiple inheritance
# example1:
class parent1:
    x=30
class parent2:
    x=50
class child(parent1,parent2):
    pass
obj=child()
print(obj.x)
# example2:
class parent1:
    x=30
class parent2:
    x=50
class child(parent2,parent1):
    pass
obj=child()
print(obj.x)
# super
# example1:
class parent1:
    def __init__(self):
        print("constructer of from parent1")
class parent2:
     def __init__(self):
        print("constructer of from parent2")
class child(parent1,parent2):
    def __init__(self):
        super().__init__()
        print("constructer of child class")
obj2=child()
# example2:
class parent1:
    def __init__(self):
        print("constructer of from parent1")
class parent2:
     def __init__(self):
        print("constructer of from parent2")
class child(parent1,parent2):
    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)
        print("constructer of child class")
obj2=child()

# hiarachical inheritance
class parent1:
    x=10
class parent2(parent1):
    pass
class child(parent1):
    pass
obj2=child()
print(obj2.x)

# hybrid inheritance
class A:
    x=10
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
obj2=D()
print(obj2.x)
# over loading
class A:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d):
        return a+b+c+d
ob=A()
print(ob.add(1,20,3,4))
# over riding
class A:
    def method1(self):
        print("method1 in class A")
class B:
    def method1(self):
        print("method1 in class B")
ob=B()
ob.method1()