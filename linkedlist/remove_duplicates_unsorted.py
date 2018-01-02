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
        prev = first_pointer
        current = prev.next_node
        while(current):
            if current.data == first_pointer.data:
                current = current.next_node
            else:
                prev.next_node = current
                prev = prev.next_node
                current = current.next_node
        first_pointer = first_pointer.next_node
    return head

if __name__ == "__main__":
    start_element = 1
    finish_element = 1
    start_node = head = hi = Node()
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

    while(hi):
        print(hi.data)
        hi = hi.next_node
    print("----------------------")
    remove_duplicates(head)
    while(head):
        print(head.data)
        head = head.next_node
