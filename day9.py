#if
n=int(input("enter a number:"))
if n== 10:
    print(f"{n} is equal to 10")
    print(type(n))
#else
Number1=int(input('enter a number:'))
Number2=int(input('enter a number:'))
if Number1 == Number2:
    print(f"{Number1} is equal to {Number2}")
else:
    print(f"{Number1} is not equal to {Number2}")
#elif
a= int(input('enter a number :'))
b = int(input('enter b number:'))
c = int(input('enter c number:'))
d = int(input('enter d number:'))
if (a>b and a>c):
    print(' a is big value')
elif (b>c and b>d):
    print('b is big value')
elif c>d:
    print('c is big value')
else:
    print('d is big value')

# write a program to check whether a number is even or odd
a= int(input('enter a number :'))
if (a%2 ==0):
    print( f' {a} is an even number')
else:
    print(f'{a} is odd number')  
# OR this code :
b=int(input("enter a number:"))
if b%2 !=0:
    print(f'{a} is odd number')
else:
    print(f'{a} is an even number')
# write a program to check to ceck given numbber is divisible by 2 and 4
a= int(input('enter a number :'))
b=int(input("enter a number:"))

if (a%2 ==0 and b%4==0):
    print( f' {a} and {b} is divisible 2 and 4 number ')
else:
    print(f'{a} and {b}is  not  divisible with 2 and 4 number')