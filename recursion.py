#FACTORIAL USING RECURSIVE FUNC
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
factorial=fact(5)
print(factorial)

#FIBNOCCI
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
f=fib(9)
print(f)

#POWER OF 2 NUMS
def pwr(n,m):
    if m==0:
        return 1
    if m==1:
        return n
    return n*pwr(n,m-1)
p=pwr(2,3)
print(p)
