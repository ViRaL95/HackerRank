class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
'''
CASE1: even length array 
[1,2,3,4,5,6]
pick 6/2 - 1 as index

[1,2,3,4,5,6,7]
pick int(7/2)


'''


def create_bst(array):
    """This method creates a binary search tree given an array in ascending order
    This is done by splitting the array up into two smaller arrays and making 
    recursive calls. The splitting
    action is done through two different cases

    CASE1: even array
    When the array is even assume that the left side of the array will an element
    less than the right side of the array 
    
    IE
    [1 2 3 4 5 6]
    left_side = [1 2]
    right_side = [4, 5, 6]
    
    CASE2: odd array
    [1 2 3 4 5 6 7]
    left_side = [1, 2, 3]
    right_side = [5, 6, 7]
    """
    if len(array) == 1:
        node = Node(array[0])
        return node
    if len(array) == 2:
        root_node = Node(array[0])
        child_node = Node(array[1])
        root_node.right = child_node
        return root_node
    if len(array) % 2 == 1:
        mid_pointer = int(len(array) / 2)
    else:
        mid_pointer = int(len(array) / 2 - 1)
    center_node = Node(array[mid_pointer])
    left_sub_tree = create_bst( array [0: mid_pointer] )
    right_sub_tree = create_bst( array[mid_pointer + 1:] )
    center_node.left = left_sub_tree
    center_node.right = right_sub_tree
    return center_node


if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    center_node = create_bst(array)
    center_node.pre_order()
    print("-------------------------")
    array.append(7)
    center_node = create_bst(array)
    center_node.pre_order() 
