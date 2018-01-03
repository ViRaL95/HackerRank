def remove_duplicates_sorted(array1):
    second_index = 0
    for index in range(len(array1) - 1):
        if array1[index] != array1[index + 1]:
            array1[second_index] = array1[index]
            second_index += 1
    array1[second_index] = array1[len(array1) - 1]
    array1 = array1[:second_index + 1]
    return array1


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
    array1 = remove_duplicates_sorted(array1)
    array1 = [13, 55, 20, 27,35, 30, 40, 35, 35, 49, 40, 49, 49, 50, 55, 55] 
    find_all_pairs_sorted(array1, 70)

