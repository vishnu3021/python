class A:
    pass
class B:
    pass
class method3(A,B):
    pass
class method4(A,B):
    pass
class method5(method4,method3):
    pass
print(method5.mro())
# overLoading
class cls:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=2):
        return a+b+c
ob =cls()
print(ob.add(1,2))