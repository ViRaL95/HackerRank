#we first select one of the elments form the list this can be any element. For example we pick the number 4. We call this number the pivot we rearrange the list such that all the elements less than the element are less than this and all elmenets greater are to the right. 


#for example Consider 7 2 1 6 8 5 3 4 and we choose 4 as the pivot 
#now  we have 2 1 3 4 8 5 7 6. This process is called partitioning. It doesnt matter if instead of 2 1 3 before 4 we hve 3 1 2. All that matters is all elements less than 4 should be to the left and ice versa.

#Now we break the problem into sorting the elements to the left of the pivot and sorting teh elements to the right of the pivot and to the left. Now unlike mergesort we dont need to create seperate arrays for each seperate part. We simply need to just keep track of the start and end index of the element

# In order to sort each sublist we have to use the partition logic again. We pick a random pivot from the sublist and we rearrange teh sublist such that all the elemnets that are less are to teh less. 

