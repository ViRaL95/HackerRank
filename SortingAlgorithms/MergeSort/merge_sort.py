"""
Merge sort is not in place, it uses additional data structures. The data that is returned is returned in a new data structure. Merge sort is the best algorithm where elements in memory are not grouped together. When you have an array you have elements that are grouped very close together in memory unliked in a linked list. 

There are two types of reference localities -- temporatl and spatial locality. Temporal loclity refers to the reuse of specifc data, and or resources. Spatial locality refers to the use of data elmeents within relatively close storage elements. Generally code has good loacality of reference if the memory accesses it makes tend to be sequentially located around asmall number of areas of memory. For example linear search over an array has great locality of reference because al the elemnets appear adjacent in memory. Linear search over a linked list has poor locality. 


"""
def merge_sort(array, low, high):
    #base case two elements
    if high > low:
        mid = low + int((high - low)/2) # (high - low)/2 = distance from center to low. low + center = actual index
        merge_sort(array, low, mid) #including mid
        merge_sort(array, mid + 1, high) #everything besides mid 
        merge(array, low, mid, high) 


def merge(array, low, mid, right):
    length_left_array = mid - low + 1#length_left_array is 1. You include the + 1 because youre including mid
    length_right_array = right - mid #length right array is 1
    left_array = [0] * length_left_array
    right_array = [0] * length_right_array
    
    for element in range(length_left_array):
        left_array[element] = array[low + element] #includes mid
    for element in range(length_right_array):
        right_array[element] = array[mid + element + 1] #doesnt include mid
    index_left = 0
    index_right = 0
    array_index = low
    while (index_left < length_left_array and index_right < length_right_array):
        if (left_array[index_left] <= right_array[index_right]):
            array[array_index] = left_array[index_left]
            index_left += 1
        else:
            array[array_index] = right_array[index_right]
            index_right += 1
        array_index += 1
    while(index_left < length_left_array):
        array[array_index] = left_array[index_left]
        index_left += 1
        array_index += 1
    while(index_right < length_right_array):
        array[array_index] = right_array[index_right]
        index_right += 1
        array_index += 1
    return    

if __name__ == '__main__':
    array = [32,1,9,6,2,19,0,-4,58]
    merge_sort(array, 0, len(array) - 1)
    print(array)
