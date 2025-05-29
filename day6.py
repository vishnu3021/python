# inbuilt method in tuple(count, index) and set{add , update, remove, pop,discard, clear,
#         set operations}
# tuple
tuple=(1,2,3,55)
t= tuple.index(55)  # returns the index of the element
print(t)
tuple2=(1,55,99,3.3,55, 66 ,55,55)
t2= tuple2.count(55)  # returns the count of the element
print(t2)
# set
# add
set1={1,2,3,'true'}
set1.add(55)  # adds an element to the set
print(set1)
# remove
s1={1,2,3,5,77, 'true'}
s1.remove('true')  # removes an element from the set, raises KeyError if not found
print(s1)
# update
s2={55,66,'55', "hi"}
s2.update('hi', "helloworld")  # updates the set with multiple elements
print(s2)
# discard it is used to remove an element from the set, does not raise an error if the element is not found
s3={1,2,3,4,5,6,22, "s3"}
s3.discard(466)  # removes the element if it exists, does not raise an error if not found
print(s3)
# clear
s4={1,2,3,4,5,6,22, "s4"}
s4.clear()  # removes all elements from the set
print(s4)  # prints an empty set
# pop
s5={22,2,3,4,5,6,22, "s5"}
popped_element = s5.pop()  # removes and returns an arbitrary element from the set
print(popped_element)  # prints the popped element
print(s5)  # prints the set after popping an element
