#When you want to find the element that appears only once when all other elements appear twice you can xor all the elements in the array. This works because when two numbers appear twice their xor is = 0 and considering xor is communative it doesnt matter what order these numbers appear in. The remaining element will be xored with 0 which will simply equal that element

def find_single_element(A):
    answer = 0
    for element in A:
        answer ^= element
    return answer


if __name__ == '__main__':
    A = [2,7,9,3,3,9,2]
    print(find_single_element(A))
