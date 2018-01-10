def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_dp(n, hash_map):
    if n == 0 or n == 1:
        return n
    if n in hash_map:
        print("yeah", n)
        print(hash_map[n])
        return hash_map[n]
    else:
        hash_map[n] = fibonacci(n-1) + fibonacci(n-2)
        return hash_map[n]

def iterative(n):
    count = n - 2
    prev2 = 0
    prev1 = 1
    if n == 0 or n == 1:
        return n
    while count >= 0:
        prev2, prev1 = prev1, prev2 + prev1
        count -= 1
    return prev1

if __name__ == '__main__':
    print(fibonacci(6))
    print(iterative(6))
    print(fibonacci_dp(6, {}))
    #0 1 1 2 3 5 8 13
