def binary_search(element, low, high, array):
    if low > high:
        return -1
    mid = low + int((high - low) / 2)
    if array[mid] == element:
        return mid
    if array[mid] > element:
        return binary_search(element, low, mid - 1, array)
    if array[mid] < element:
        return binary_search(element, mid + 1, high, array)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 9, 20]
    print(binary_search(7, 0, len(array) - 1, array))
