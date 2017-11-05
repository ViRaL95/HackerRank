class Node:
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node

def reverse(head):
    if not head or not head.next_node:
        return head
    last = None
    first_pointer = head
    while(first_pointer):
            second_pointer = first_pointer.next_node
            first_pointer.next_node = last
            last = first_pointer
            first_pointer = second_pointer
    return last

if __name__=='__main__':
    head = temp = Node()
    temp.data = 5
    for i in range(6,10):
        next_node = Node()
        next_node.data = i
        temp.next_node = next_node
        temp = temp.next_node
    pointer = reverse(head)
    while (pointer):
        print("entered")
        print(pointer.data)
        pointer = pointer.next_node

