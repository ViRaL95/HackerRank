def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
value = fibonacci(n)
print(value)
