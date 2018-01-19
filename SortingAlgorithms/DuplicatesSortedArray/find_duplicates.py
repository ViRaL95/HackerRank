def remove_duplicates_sorted(array1):
    """ This function removes duplicates from the sorted array by iterating through
    the array and having a current 'pointer' and a 'next' pointer. If the value of the
    next pointer is not equal to the current pointer then we know there does not exist
    a duplicate element with the value that the current pointer holds. We can have a
    third pointer which only increments when it has found that the element next to it
    is not equal to itself. The third pointer will then replace the value at which
    it currently points at to the non duplicate value.

    MUST NOTE: Previously I tried to perform the following instead of returning a new
    array :
    array1 = array1[:second_index + 1]
    My assumption was that considering arrays are mutable objects in Python, this array
    would chnage in memory in the calling function as well. However, if one compares
    the id of array 1 before and after this operation occurs we will find that they are
    different, meaning they are different objects on the heap entirely and the inital
    array in the calling function will not be changed
    """
    second_index = 0
    for index in range(len(array1) - 1):
        if array1[index] != array1[index + 1]:
            array1[second_index] = array1[index]
            second_index += 1
    array1[second_index] = array1[len(array1) - 1]
    return array1[:second_index + 1]


def find_all_pairs_sorted(array1, sum_):
    count = 0
    hash_set = set()
    for element in array1:
        hash_set.add(element)
    
    for element in array1:
        if sum_ - element in hash_set:
            count += 1
        


if __name__ == '__main__':
    array1 = [13, 20, 27, 30, 35, 35, 40, 49, 49, 50, 55, 55] 
    yai = remove_duplicates_sorted(array1)
    print(yai)
