'''
a way to implement an algorithm for the greatest common divisor problem 

'''
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a %b) 


# example 
print(gcd(357, 234))