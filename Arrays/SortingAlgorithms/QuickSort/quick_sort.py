#Our pivot can be any element in the array, I generally tend to pick the last element as the pivot. We like to have all elements to the left of the pivot to be less than or equal to it, and all elements to the right ot be greater than or equal to it. This algorithm has constant space and n*logn complexity.



def QuickSort(A, start, end):
    if start >= end:
        return
    partition_index = partition(A, start, end)
    QuickSort(A, start, partition_index - 1)
    QuickSort(A, partition_index + 1, end)

def partition(A, start, end):
    pivot = A[end]
    partition_index = start
    for element in range(start, end):
        if A[element] <= pivot:
            A[element], A[partition_index] = A[partition_index], A[element]
            partition_index += 1
    A[partition_index], A[end] = A[end], A[partition_index]
    return partition_index

def QuickSort2(array, start, end):
    if start > end:
        return
    partition_index = partition2(array, start, end)
    QuickSort2(array, start, partition_index - 1)
    QuickSort2(array, partition_index + 1, end)


def partition2(array, start, end):
    pivot = array[end]
    partition_index = start
    for element in range(start, end):
        if array[element] <= pivot:
            array[element], array[partition_index] = array[partition_index], array[element]
            partition_index += 1
    array[partition_index], array[end] = array[end], array[partition_index]
    return partition_index

if __name__ == '__main__':
    A = [7,6,6,5,4,3,2,2,1,0,0]
    QuickSort2(A, 0, len(A) - 1)
    print(A)

