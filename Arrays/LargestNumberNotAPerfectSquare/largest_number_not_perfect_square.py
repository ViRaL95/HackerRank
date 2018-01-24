import math

def find_largest_number_not_perfect_square(array):
    """ This method finds the largest number in an array that is not a perfect square.
    """
    max_ = 0
    for element in array:
        if not_perfect_square(element):
            max_ = max(element, max_)
    return max_

def not_perfect_square(element):
    sqrt_element = int(math.sqrt(element))
    if sqrt_element ** 2 != element:
        return True
    return False

if __name__ == '__main__':
    print(find_largest_number_not_perfect_square([1,4,7,99,34,2]))
    
