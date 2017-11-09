# 1 6 2 6 6 5 4 
#1 6 2 
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def remove_duplicates(head):
    if not head or not head.next_node:
        return head
    first_pointer = head
    while(first_pointer.next_node):
        second_pointer = first_pointer.next_node
        value = first_pointer.data
        new_linked_list = None
        while(second_pointer):
            if second_pointer.data != value:
                if not new_linked_list:
                    head_b = new_linked_list = Node()
                    new_linked_list.data = second_pointer.data
                else:
                    new_node = Node()
                    new_node.data = second_pointer.data
                    new_linked_list.next_node = new_node
                    new_linked_list = new_linked_list.next_node
            second_pointer = second_pointer.next_node
        first_pointer.next_node = head_b
        first_pointer = first_pointer.next_node
    return head

if __name__ == "__main__":
    start_element = 1
    finish_element = 1
    start_node = head = Node()
    start_node.data = 0
    while (finish_element <= 5):
        start_element = 1
        while (start_element <= finish_element):
            next_node = Node()
            next_node.data = start_element
            start_node.next_node = next_node
            start_node = start_node.next_node
            start_element += 1
        finish_element += 1
    k=remove_duplicates(head)
    while(k):
        print(k.data)
        k = k.next_node