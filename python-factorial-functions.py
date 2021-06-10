import time as tm

def factorial(n):
    f = 1
    for i in range(2,n+1):
        f = f*i
    
    return f

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

t1 = tm.time()
print(factorial(50))
t2 = tm.time()
print(fact(50))
t3 = tm.time()