# Prime Numbers | 
# code -1
# prime numbers printing
n=eval(input("enter a number:"))
# print(type(n))
for i in range(2,n):
    if n%i==0:
        print('not a prime number')
        break
else:
    print("prime  number")



# adding Numbers

# adding numbers
n=int(input("enter a number:"))
x=str(n)
sum=0
# print(type(x))
for i in x:
    # print(i)
    sum=sum+int(i)
print(sum)
# reverse string
r=int(input("enter a number:"))
# r=87
sum=" "
while r!=0:
    rem=r%10
    sum+=str(rem)
    r=r//10
print(sum)