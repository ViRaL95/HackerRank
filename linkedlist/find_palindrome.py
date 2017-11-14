class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def find_palindrome(head):
    double = single = head
    pointer = head
    counter = 0
    while(double.next_node and double.next_node.next_node):
        double = double.next_node.next_node
        single = single.next_node
    mid = single
    current = single.next_node
    while current:
        temp = current.next_node
        current.next_node = single
        single = current
        current = temp
    while mid is not single:
        if pointer.data != single.data:
            return False
        single = single.next_node
        pointer = pointer.next_node
    return True



if __name__ == '__main__':
    start = linked_list = Node(data="r")
    new_node = Node(data="a")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    new_node = Node(data="c")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    new_node = Node(data="e")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    new_node = Node(data="c")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    new_node = Node(data="a")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    new_node = Node(data="r")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    print(find_palindrome(start))
    start = linked_list = Node(data="a")
    new_node = Node(data="a")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    print(find_palindrome(start))
