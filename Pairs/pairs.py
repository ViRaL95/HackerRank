#this is the pairs example on hackerrank 
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    hash_map = {}
    counter = 0
    for element in a:
        hash_map [element] = True
    for element in a:
        remove = False
        if ((element - k) in hash_map):
            counter += 1
            remove = True
        if ((element + k) in hash_map):
            counter += 1
            remove = True
        if remove:
            hash_map.pop(element)
    return counter
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
