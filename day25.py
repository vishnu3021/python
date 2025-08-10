# object methods | class methods | static methods
# object method
class bank():
    bankName="rbi"
    ROI=0.5
    def __init__(self,name,acc,mbno,add,bal):
        self.name=name
        self.acc=acc
        self.mbno=mbno
        self.add=add
        self.bal=bal
    def checkbalance(self):
        print(f'{self.name} avaliable balance is {self.bal}')
    def deposite(self,amount):
        self.bal+=amount
        print(f'amount is sucessfully deposite')
    def withdraw(self,amount):
        if self.bal>=amount:
            self.bal-=amount
            print("amount is sucessfully withdrawn!!")
        else:
            print("insufficent balance!!")
ob=bank("sravya", "2024563",78654123,"kadapa",8000)
ob.withdraw(500)
ob.checkbalance()





# class method    
class Bank():
    bankName="rbi"
    ROI=0.5
    def __init__(self,name,accid,branch,mobileNo,address,balance):
        self.name=name
        self.accid=accid
        self.branch=branch
        self.mobileNo=mobileNo
        self.address=address
        self.balance=balance
    @classmethod
    def clsmethod(cls,updateRoi):
        cls.ROI=updateRoi
        print(f'updated roi is:{updateRoi}')
ob=Bank("sravya", "2024563", "kadapa", 78654123, "kadapa", 8000)
print(ob.name,ob.accid,ob.branch,ob.mobileNo,ob.address,ob.balance)
ob.clsmethod(1.0)    

# static method
