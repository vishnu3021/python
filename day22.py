# all type of fumctions
# 1) position function
#2)  key function
#3) default function
#4) value length non key word function
#5) value length  key word function


# 1) position function
def postion(a,b,c):
    print(f'a is {a}, b is {b}, c is {c}')
#2)  key function
def keyFunction(name, gender, age):
    print(f'name is {name}')
    print(f'age is {age}')
    print(f'gender is {gender}')
keyFunction(name='vishnu',age=23, gender="Male")
#3) default function
def defaultFunction(a=0, b=20, c=50, d=100):
    print(f' a is {a}, b is {b}, c is {c} and d is {d}')
defaultFunction(a=2,c=100)
#4) value length non key word function
def valeLeng(*name):
    print(f'{name}')
valeLeng("vishnu", "vardhan")
#5) value length  key word function
def valeLeng2(**name):
    print(f'{name}')
valeLeng2(name="vishu", age=22, place="hyderbad", passion="coding")
# #6) lambda function
# def lambdaFunction(x, y):
#     return (lambda x, y: x + y)(x, y)   
# print(lambdaFunction(10, 20))
