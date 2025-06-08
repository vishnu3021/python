# code1:
for i in range(5):
    print("Hello World!,", end=" ")
# code2:
n=6
while n<=10:
    print("hey ptython")
    n=n+1
# NESTED lOOP:
row=5
col=3
for i in range(row):
    for j in range(col):
        if i%2==0:
            print('*', end=" ")
        else:
            print("vi", end=" ")
    print()
# code3:
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==i or i==n-1 :
            print("*", end='')
        else:
            print("", end= " ")
    print()
# code4:
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==i or i==n-1 or j==n-1  or i+j==n-1:
            print("*", end='')
        else:
            print("", end= " ")
    print()
# code5:
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*", end='')
        else:
            print("", end= " ")
    print()
# code6:
n=5
st=1
for i in range(n):
    for j in range(st):
        print('*', end=" ")
    print()
    st=st+1
# code7:
n=5
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or j==2  or i==2 or j==4 or i==4:
            print("*", end=" ")
        else:
            print("!", end=" ")
    print()