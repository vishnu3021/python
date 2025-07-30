# adding numbers
# factorial
# fib series numbers
# adding numbers
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
print(sum(122))
# factorial
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
# fib series numbers
def fib(n):
    if n==0 or n==1:
        return n+1
    return fib(n-1)+fib(n-2)
print(fib(3))