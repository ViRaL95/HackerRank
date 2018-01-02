class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
#this is done changing the original linked list
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

#without changing the original linked list
def find_palindrome_wo(head):
    stack = []
    temp = slow = fast = head
    stack.append(head.data)
    counter = 0
    while (temp):
        counter += 1
        temp = temp.next_node
    if counter == 2:
        return fast.data == fast.next_node.data
    while (fast and fast.next_node):
        slow = slow.next_node
        fast = fast.next_node.next_node
        stack.append(slow.data)
    if counter % 2 == 1:
        element = stack.pop()
        slow = slow.next_node
    counter = 0
    length_of_stack = len(stack)
    while (slow):
        counter += 1
        element = stack.pop()
        if element != slow.data:
            return False
        slow = slow.next_node
    if counter != length_of_stack:
        return False
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
    print(find_palindrome_wo(start))
    start = linked_list = Node(data="a")
    new_node = Node(data="a")
    linked_list.next_node = new_node
    linked_list = linked_list.next_node
    print(find_palindrome_wo(start))
