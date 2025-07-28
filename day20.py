# sum, 
L=[22,33,55]
print(sum(L))
# examle for sum using logic
# example1:
L=[11,5,80,56]
sum=0
for i in L:
    sum=sum+i
print(sum)
# example2:
l2=[11,5,80,56]
add=0
for j in range(len(l2)):
    add=add+L[j]
print(add)
# max number 
# l=[50,99.9,99.8,5,0,4,65,15,20,80]
j=l[0]
for i in range(1,len(l)):
    if j< l[i]:
        j=l[i]
print(j) 
# min numbers,
list=[0,22,55,10,1,5]
d=list[0]
for i in range(0,len(list)):
    if d>list[i]:
        d=list[i]
print(d)
# sort method
sort=[55,0,55,10,50,2,6,7,9,8]
for a in range(0,len(sort)):
    for b in range(0, len(sort)-1):
        if sort[b]>sort[b+1]:
            sort[b],sort[b+1]=sort[b+1],sort[b]
print(sort)