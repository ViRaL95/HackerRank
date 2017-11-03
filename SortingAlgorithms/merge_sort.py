class MergeSort:
    def __init__(self):
        array = [45,23,11,89,77,98,4,28,65,43]
        self.sort(array)
        for element in array:
            print(element)

    
    def sort(self, array):
        length = len(array)
        print(length)
        self.mergeSort(0, length -1)

    def mergeSort(self, lower_index, higher_index):
        if (lower_index < higher_index):
            print("entered")
            middle = lower_index + (higher_index - lower_index)/2
            print("yo")
            self.mergeSort(lower_index, middle)
            print("ah")
            self.mergeSort(middle + 1, higher_index)
            print("daf")
            self.mergeParts(lower_index, middle, higher_index)

    def mergeParts(self, lower_index, middle, higher_index):
        for i in range (lower_index, higher_index + 1):
            temp_array[i] = array[i]
            print("start")
        i = lower_index
        j = middle + 1
        k = lower_index
        while(i <= middle and j<=higher_index):
            if temp_array[i] <= temp_array[j]:
                array[k] = temp_array[i]
                i+=1
            else:
                array[k] = temp_array[j]
                j += 1
            k+=1
        while (i<= middle):
            array[k] = temp_array[i]
            k+=1
            i+=1

if __name__ == '__main__':
    MergeSort()
