def largest_subarray_with_equal_0s_and_1s(array):
    """This method finds the largest subarray with equal 0s and 1s.
    """
    max_ = 0
    for index, element in enumerate(array[:-1]):
        number_of_zeros = 0
        number_of_ones = 0
        for index2 in range (index, len(array)):
            if array[index2] == 0:
                number_of_zeros += 1
            if array[index2] == 1:
                number_of_ones += 1
            if number_of_ones == number_of_zeros:
                max_ = max(number_of_zeros + number_of_ones, max_)
    return max_


if __name__ == '__main__':
    print(largest_subarray_with_equal_0s_and_1s([1,1,1,1,1,0,0,0,0,1,0,0]))
