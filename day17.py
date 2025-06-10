# day17:
n=5
st=1
num=5
for a in range(n):
     num=num+1-st
     for b in range(st):
        print(num, end=" ")
num+=1
print()
sp-=1
st+=1
#code-2
n=5
st=1
num=5
for a in range(n):
	num=n+1-st
for c in range(st):
	print(num, end="")
	num+=1
print()
st+=1