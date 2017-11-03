def binary_search(array, left_index, right_index, target):
    if right_index>=left_index:
        mid = left_index + int((right_index - left_index)/2)
        print(mid)
        if array[mid]==target:
            return mid
        elif array[mid] > target:
            return binary_search(array, left_index, mid-1, target)
        else:
            return binary_search(array, mid +1, right_index, target)
    else:
        return -1

if __name__ == '__main__':
    array = [1,3,5,7,9,11,13,15]
    print(binary_search(array, 0, len(array)-1, 13))
