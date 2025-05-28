# List inbuilt methods
# append
# extend
# insert
# remove
# pop
# clear
# index
# count


# append
List = ["vishnu", "vardhan"]
List.append("Reddy")
print(List)
# extend
extend=["reddy", "hello"]
extend.extend("vardhan")
print(extend)
extend.extend([1,2,3,4])
print(extend)
# insert
_i=[1,2,3,4]
_i.insert(1,60)
print(_i)
# remove
re= ["hello", "this " "is", "vishnu"]
re.remove("hello")
print(re)
# pop
pop_list=["1",'2', '8','3', '4']
pop_list.pop(2) #assing index 2
print(pop_list)
# clear
clear_list = ["hello", "world", "vishnu"]
clear_list.clear()
print(clear_list)
# index
list_index=["hello", "world", "vishnu"]
print(list_index.index("vishnu"))  # returns the index of "vishnu"
# count
count = ["hello", "world", "vishnu", "hello"]
c2 =count.count("vishnu") # returns the count of "hello"
print(c2)