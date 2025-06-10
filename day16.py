# code-1
# n=int(input("endera number:"))
n=5
for a in range(n):
    for b in range(n):
        if a==0 or b==0 or b==n-1 or a==n-1 or a==b or a+b==n-1 or a==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
print()
# code-2
n=3
sp=n-1
st=1
for a in range(n):
    for b in range(sp):
        print(" ", end=" ")
    for c in range(st):
        print('*', end=' ')
    print()
    st+=2
    sp-=1
# code-3(diamond pattern)
sp=n//2
st=1
for a in range(n):
    for b in range(sp):
        print(' ',  end=" ")
    for c in range(st):
        print("*", end=" ")
    print()
    if a<2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
# code-4(numbers patterns):
n=5
num=1
for a in range(n):
    for b in range(n):
        print(num, end=" ")
    print()
    num=num+1
# code-5
n=5
num=1
for a in range(n):
    for b in range(n):
        print(num, end="")
        num+=1
    print()
    num=1
# code-6
n=5
sp=0
st=n
num=5
for a in range(n):
    for b in range(sp):
        print(' ', end="")
    for c in range(st):
        print(num,end=" ")
        num-=1
    print=()
    st-=1
    sp+=1
    num=5