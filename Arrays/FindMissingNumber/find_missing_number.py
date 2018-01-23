def find_missing_number(array):
    """ This method finds the missing number given an array containing elements from 1 to n
    in any order. Only one number is missing from this array. First step is to find the actual sum of    all elements summed from 1 to n, which is equal to n * (n + 1) / 2.  Considering there are n - 1     elements in the array, the calculated formula will be (n + 1)*(n + 2)/2, where n is 
    the length of the array. After we have finished calculating the actual sum of the elements from 1    to n we subtract the sum of the elements in the array from this. This new value is the missing el    element.
    """
    actual_sum = (len(array) + 1)*(len(array) + 2) / 2
    sum = 0
    for element in array:
        sum += element
    return actual_sum - sum

if __name__ == '__main__':
    print(find_missing_number([1,2,4,3,7,6,5,9]))
