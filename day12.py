# range:
r=range(20)
print(tuple(r))
# range with start and end
r=range(5,20)
print(tuple(r))
# range with start, end and step
r=range(5,20,2)
print(tuple(r))
# range with negative step
r=range(10,0,-1)
print(list(r))

# for loop 
# for varibleName in iterable:
for char in 'python':
    print(char)
str= "hello world!!"
for str2 in str:
    print(str2)
dict={'a':20, 'b':30, 'c':50}
for key, value in dict.items():
    print(key, value)
# to print values only
dict={'a':20, 'b':30, 'c':50}
for Dd in dict.values():
    print(Dd)
# to print keys only
dict={'a':20, 'b':30, 'c':50}
for Dd in dict.keys():
    print(Dd)
#  to print bot keys and values
dict={'a':20, 'b':30, 'c':50}
for key, value in dict.items():
    print(key, value)
# for varibleName in range(start, end, step):
for char in range(0,30):
    print(char, end=",")

for char2 in range(30,20,-1):
    print(char2)
print("end of for Loop")
# for loop with list
List=[]
for i in range(15+1):
    List.append(i)
print(List)