# list and dictionay problems
# lsit
l=[11,12,13,14,11,12,20]
r=[]
for i in l:
    if i not in r:
        r.append(i)
print(r)
# example-2:
l2=[21,32,13,14,21,32,13]
r2=[]
for i in range(len(l2)):
    if l2[i] not in r2:
        r2.append(l2[i])
print(r2)

# dictionary
d={'a':20, 'b':30, 'c':40}
val=20
for key, values in d.items():
    if val==values:
        print(f' {key}:{values}')




# write a program to print no of times each character repeated in string

s="ENGINEERING"
d={}
for a in s:
    if a not in d:
        d[a]=1
    else:
        d[a]+=1
print(d)


# write a program to print most frequent character in string
s="ENGINEERING"
d={}
for a in s:
    if a not in d:
        d[a]=1
    else:
        d[a]+=1
lst=list(d.values())
h=lst[0]
for a in range(1, len(lst)):
    if h<lst[a]:
        h=lst[a]
for k,v in d.items():
    if v==h:
        print(k)
# write a program to print frequently occured word in string?
L= "WE DONT PRASCTICE BUT WE WANT JOB "
s=L.split()
# print(s)
d={}
for a in s:
    if a not in d:
        d[a]=len(a)
# print(d)
L=list(d.values())
# print(L)
h=L[0]
for a in range(1,len(L)):
    if h<L[a]:
        h=L[a]
for k,v in d.items():
    if v==h:
        print(k)
