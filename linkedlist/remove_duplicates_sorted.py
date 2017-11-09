class Node:
    def __init__ (self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def remove_duplicates(linked_list):
    if not linked_list or not linked_list.next_node:
        return linked_list
    pointer_a = linked_list
    while (linked_list.next_node):
        if linked_list.data == linked_list.next_node.data:
            duplicate = linked_list.next_node
            next_value = None
            while(duplicate.next_node):
                if (not(duplicate.next_node.data == duplicate.data)):
                    next_value = duplicate.next_node
                    break
                duplicate = duplicate.next_node
            linked_list.next_node = next_value
        else:
            linked_list = linked_list.next_node
    return pointer_a


if __name__ == "__main__":
    first_pointer = head = Node()
    head.data = 0
    index = 1 
    loop_counter = 0
    while (index <= 6):
        nodea = Node()
        nodea.data = index
        head.next_node = nodea
        loop_counter += 1
        head = head.next_node
        if loop_counter == 2:
            index += 1
            loop_counter = 0
    linked_list = remove_duplicates(first_pointer)
    while (linked_list):
        print(linked_list.data)
        linked_list = linked_list.next_node

