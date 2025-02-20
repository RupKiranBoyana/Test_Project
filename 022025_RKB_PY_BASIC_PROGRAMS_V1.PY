## Reversing a string 

def reverse_string(s):
    return s[::-1]

s = "Python"
print (reverse_string(s)) 

## Check if a number is prime or not 

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))

## Find the factorial of a number 

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5))

## Check if a string is palindrome 

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

## Find the fibonacci series up to N terms 

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end="")
        a, b = b, a + b  
fibonacci(7)   




