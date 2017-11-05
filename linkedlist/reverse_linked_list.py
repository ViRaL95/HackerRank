class Node:
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node

def reverse(head):
    print("d")
    if not head or not head.next_node:
        return head
    first_pointer = head
    second_pointer = head.next_node
    while(first_pointer.next_node):
            second_pointer = first_pointer.next_node
            temp = second_pointer.next_node
            second_pointer.next_node = first_pointer
            first_pointer = second_pointer
            second_pointer = temp
            print(first_pointer.data)
            print(second_pointer.data)
            print("-----------------")
    return first_pointer

if __name__=='__main__':
    head = temp = Node()
    temp.data = 5
    for i in range(6,10):
        next_node = Node()
        next_node.data = i
        temp.next_node = next_node
        temp=temp.next_node
    pointer = reverse(head)
    while (pointer):
        pointer = pointer.next_node

