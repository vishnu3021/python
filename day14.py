# break
# code 1 using for loop 
n=int(input("enter a number:"))
print(type(n))
for i in range(n,10+1):
    if i >=10:
        break
    print(i)
# code 2 using while loop
n=1
while n<=8:
    if n==8:
        break
    print(n)
    n=n+1
print('out of while loop')
# code 3: usinge continue with for loop:
n= 25
for i in range(0,26):
    if i%5==0:
        continue
    print(i)

# one more example:
start=eval(input("enter a strating number:"))
end=eval(input("enter a end number:"))
for i in range(start,end):
    if i==10:
        break
    print(i)
print("out side of the loop")
# code 4 using while loop with continue:
n=1
while n<=15:
    if n==11:
        break
    print(n)
    n=n+1
print("out side of the loop")
# one more example:
insertNum=int(input('enter a number:'))
while insertNum<=20:
    if insertNum==13:
        break
    print(insertNum)
    insertNum+=1
print("the end ")