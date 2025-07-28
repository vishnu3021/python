# number program nd string problems
# amstrong number:
n=153
num=n
s=str(n)
l=len(s)
sum=0
while n!=0:
    rem=n%10
    sum=sum+rem**l
    n=n//10
print(sum)
if num==sum:
    print(f'{sum} is an amstrong number')
else:
    print(f'{sum} is not an amstrong number')
# exammple2:
n=int(input("enter a number:  "))
num=n
s=str(n)
l=len(s)
sum = 0
while n!=0:
    rem=n%10
    sum=sum+rem**l
    n=n//10
print(sum)
if sum==num:
    print(f"{sum} is an amstrong number")
else:
    print(f"{sum} is not an amstrong number")
# Disarium numbers:
n=int(input("enter a number:  "))
num=n
s=str(n)
l=len(s)
sum = 0
while n!=0:
    rem=n%10
    sum=sum+rem**l
    n=n//10
    l=l-1
print(sum)
if sum==num:
    print(f"{sum} is a Disarium  number")
else:
    print(f"{sum} is not a Disarium  number")
# factrorial nmber:
num=5
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)
# string problems::::
s="python"
l=len(s)
# print(l)
for a in range(len(s)):
    print(s[a], end=" ")
# odd and even positions printing:
s="python"
even=""
odd=""
for i in range(len(s)):
    if i%2==0:
        even=even+s[i]
    else:
        odd=odd+s[i]
print(odd)
print(even)
# string number:
# string reverse:
s="vishnu"
for i in range(-1, -(len(s)+1), -1):
    print(s[i], end="")
# palindrome number:
name="s madam s"
reverse=""
for i in range(-1,-(len(name)+1),-1):
    reverse=reverse+name[i]
# print(reverse, end="")
if reverse==name:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")

# finding vowles in a string:
v="vishnuuuu"
t=""
vol="aeiouAEIOU"
for a in v:
    if a in vol:
        t+=a
print(t)