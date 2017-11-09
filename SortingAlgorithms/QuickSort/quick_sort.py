#we first select one of the elments form the list this can be any element. For example we pick the number 4. We call this number the pivot we rearrange the list such that all the elements less than the element are less than this and all elmenets greater are to the right. 


#for example Consider 7 2 1 6 8 5 3 4 and we choose 4 as the pivot 
#now  we have 2 1 3 4 8 5 7 6. This process is called partitioning. It doesnt matter if instead of 2 1 3 before 4 we hve 3 1 2. All that matters is all elements less than 4 should be to the left and ice versa.

#Now we break the problem into sorting the elements to the left of the pivot and sorting teh elements to the right of the pivot and to the left. Now unlike mergesort we dont need to create seperate arrays for each seperate part. We simply need to just keep track of the start and end index of the element

# In order to sort each sublist we have to use the partition logic again. We pick a random pivot from the sublist and we rearrange teh sublist such that all the elemnets that are less are to teh less. 

#The quick sort algorithm uses divide and conquer to gain the same advantages as merge sort (n logn) but without additional storage. When the list is not able to be divded by half then the performance diminishes. 


def QuickSort(A, start, end):
    if (start >= end):
        return 
    partition_index = Partition(A, start, end)
    #divide and conquer methodology
    QuickSort(A, start, partition_index -1 )
    QuickSort(A, partition_index + 1, end)


def Partition(A, start, end):
    #The partition index is essentially used to reprsent the partition
    #Elements in the array are iterated through and compare against the
    #pivot value if they are smaller then the value at the partitoin index 
    #and the element in the array we are currently at within the iteration are 
    #swapped. Finally because the partition index is just a representation of 
    # the actual partition we swap the two variables
    pivot = A[end]
    partition_index = start
    for i in range(start, end):
        if A[i] <= pivot and partition_index != i:
            temporary = A[i]
            A[i] = A[partition_index]
            A[partition_index] = temporary
            partition_index += 1
    temporary = A[partition_index]
    A[partition_index] = A[end]
    A[end] = temporary
    return partition_index


if __name__ == '__main__':
    A = [7,6,6,5,4,3,2,2,1,0,0]
    QuickSort(A, 0, len(A) - 1)
    for value in A:
        print (value)
