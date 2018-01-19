"""
Merge sort is not in place, it uses additional data structures. The data that is returned is returned in a new data structure. Merge sort is the best algorithm where elements in memory are not grouped together. When you have an array you have elements that are grouped very close together in memory unliked in a linked list. 

There are two types of reference localities -- temporatl and spatial locality. Temporal loclity refers to the reuse of specifc data, and or resources. Spatial locality refers to the use of data elmeents within relatively close storage elements. Generally code has good loacality of reference if the memory accesses it makes tend to be sequentially located around asmall number of areas of memory. For example linear search over an array has great locality of reference because al the elemnets appear adjacent in memory. Linear search over a linked list has poor locality. 


"""
def merge_sort(array, low, high):
    if low >= high:
        return
    mid = low + int((high - low)/2)
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)
    merge(low, mid, high, array)

def merge(low, mid, high, array):
    #We tak the left and right array and then we create a new array
    left_array = array[low: mid + 1]
    right_array = array[mid + 1: high + 1]

    right_index = 0
    left_index = 0
    array_index = low
    while  left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            array[array_index] = left_array[left_index]
            left_index += 1

        else:
            array[array_index] = right_array[right_index]
            right_index += 1

        array_index += 1

    while left_index < len(left_array):
        array[array_index] = left_array[left_index]
        left_index += 1
        array_index += 1

    while right_index < len(right_array):
        array[array_index] = right_array[right_index]
        right_index += 1
        array_index += 1
    return

if __name__ == '__main__':
    array = [32,1,9,6,2,19,0,-4,58]
    #merge_sort(array, 0, len(array) - 1)
    merge_sort(array, 0, len(array) - 1)
    print(array)
