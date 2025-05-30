# inbuilt method in dictionaary(add, update, pop, popItem, get, getDefault, formKeys)
# add
d={}
d['age']= 20  # this will raise an error, as dictionaries do not have an 'add' method
print(d)
# update
D={'name':'vishnu', 'age':20}
D.update({"place":"kurnool"})
print(D)  # updates the dictionary with the new key-value pair
    #  or
D1={'name':'vardhan Reddy', 'age':20}
D2={'age':'kurnool'}
D1.update(D2)  # updates D1 with the key-value pairs from D2
print(D1)  # prints the updated dictionary
# pop
pop= {'class':'B.Tech', 'year':2023, 'branch':'CSE'}
pop.pop("class")
print(pop)
# popItem, 
popItem= {'place':'nandikotkur', 'State':"AP", "pinCode":518401}
popItem.popitem()  # removes and returns the last inserted key-value pair from the dictionary
print(popItem)  # removes and returns the last inserted key-value pair from the dictionary
# get, 
get={"name":"name", "age":20}
G = get.get('name')
print(G)  # retrieves the value associated with the key 'name'
# getDefault, 
getDefault = {"name":"GvVR", "age":23}
G1 = getDefault.get('D', 'Reddy')  # retrieves the value associated with 'name', or returns 'default_value' if 'name' is not found
print(G1)  # prints the value associated with 'name'
print(getDefault)  # prints the original dictionary
# formKeys error is their is no inbuilt method called 'formKeys' in Python dictionaries.
# formKeys = {'name':'GvVR', 'age':23}
# keys = formKeys.formkeys()  # retrieves the keys of the dictionary
# print(keys)  # prints the keys of the dictionary