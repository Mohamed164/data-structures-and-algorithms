'''
A recursive approach to implementing the fibonacci series 

This is a BAD approach since it takes a very long time to execute 

takes a ridiculously long time 
'''
def fib_recurr(n): 
    if n <= 1:
        return n
    else:
        return fib_recurr(n-1) + fib_recurr(n -2)

