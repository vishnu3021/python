# airthmatic operators
a = '10'
b = '22'
print(a+b)
# print(a*b) #error, as multiplication is not defined for strings in Python
# print(a/b) #error, as division is not defined for strings in Python
# print(a-b) #error, as subtraction is not defined for strings in Python
A= 2
B = 3
print(A**B)  # exponentiation operator, raises A to the power of B
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A/B)
print(A%B)  # modulus operator, returns the remainder of the division of A by B
#Assignment operators(=, ==,<,>,<=,>=,!=)
# Assignment operators are used to assign values to variables.
V,I = 20,10  # assigns the value 10 to the variable V and I
print(V, I)
print(V == I)  # checks if V is equal to I, returns False
print(V>I)
print(V<I)  # checks if V is less than I, returns True
print(V!= I)  # checks if V is not equal to I, returns True
print(V<=I)
print(V>=I)
#logical operators (and, or, not)
# and operator
print(True and  True)
print(False and False)
print(True and False)
# or operator
print(False or True)
print(True or True)
# not operator
print (not True)
print(not False)
# bitwise operators (&, |, ^, ~, <<, >>)
# Bitwise operators are used to perform bit-level operations on integers.
# & (bitwise AND)
print(5 & 3)
# bitwise or operator (|)
print(5 | 3)  # performs bitwise OR operation on 5 and 3
# bitwise xor operator (^)
print(10 ^ 6)
print(2 ^ 3)
# bitwise not operator (~)
print(~2)
# bitwise left shift operator (<<)
print(8 << 1)
# bitwise right shift operator (>>)
print(8 << 3)
# identifiers(is , is not)
# Identifiers are used to check the identity of objects in Python.
z= 22
v = 55
print(z is 22)
print (z is  v)
print( z is not v)
# menbership operators (in, not in)
str = "Hello, World!"
print("HI" in str)
print("Hello" in str)

