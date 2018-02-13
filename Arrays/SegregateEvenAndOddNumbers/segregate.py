def segregate_even_and_odd(array):
    left = 0
    right = len(array) - 1
    while left < right:

        while array[left] %2 == 0 and left < right:
            left += 1

        while array[right] % 2 == 1 and left < right:
            right -= 1

        array[left], array[right] = array[right], array[left]        


if __name__ == '__main__':
    array = [12, 34, 45, 9, 8, 90, 3]
    segregate_even_and_odd(array)
    print(array)
    array = [3,4,5,6,7,8,9,10,12,13]
    segregate_even_and_odd(array)
    print(array)
