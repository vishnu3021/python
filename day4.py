# inbuilt string methods
# upper
# lower
# swapcase
# title
# capitalize
# index
# rindex
# find
# count
# split
# replace
# Example usage of string methods

# upper
str1 = "hello world"
str1.upper()
print(str1)
# lower
lower_str="HELLO VISHNU"
print(lower_str.lower())
# swapcase
swap="HelLo vIShNU"
print(swap.swapcase())
# title
title="vishNu stArted leArning pyThon "
print(title.title())
# capitalize
cap="hELLO pYtHon programming"
print(cap.capitalize())
# index
indexStr="python programming"
print(indexStr.index('programming'))  # Returns the index of the first occurrence of 'programming'  
# rindex
print(indexStr.rindex('g'))  # Returns the index of the last occurrence of 'g'
# find
findStr="june"
print(findStr.find('u'))  # Returns the index of the first occurrence of 'u', or -1 if not found
print(findStr.find('z'))
# count
countStr = "vishnu vardhan Reddy G"
print(countStr.count('d'))  # Counts the occurrences of 'd'
# split
splitStr="banana,apple,orange"
print(splitStr.split('a'))  # Splits the string at 'a' and returns a list
# replace
replaceStr = "hello world"
print(replaceStr.replace('o', 'd'))  # Replaces 'o' with 'd' in the string
#slice
sliceStr= "hello world"
print(sliceStr[0:])  # Slices the string from index 3 to the second last character
print(sliceStr[0:5])  # Slices the string from index 0 to 4
# rslice
sliceStr = "vishnu"
print(sliceStr[0:5:2])  # Slices the string from index 0 to 4 with a step of 2 ouptput: 'vhn'
# strip
stripStr = "Apple      orange        and              banana" 
print( stripStr.strip( ))  # Removes leading and trailing whitespace
