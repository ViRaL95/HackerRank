class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def add_forward_linked_list(head1, head2):
    length1 = calculate_length(head1)
    length2 = calculate_length(head2)
    if length2 > length1:
        difference = length2 - length1
        append_zeros(head1, difference)
    elif length1 > length2:
        difference = length1 - length2
        append_zeros(head2, difference)
    prev1 = None
    prev2 = None
    start1 = head1
    start2 = head2
    while(start1 and start2):
        temp1 = start1.next_node
        start1.next_node = prev1
        prev1 = start1        
        start1 = temp1

        temp2 = start2.next_node
        start2.next_node = prev2
        prev2 = start2
        start2 = temp2

    new_linked_list = None
    carry = 0
    while(prev1 and prev2):
        value = (prev1.data + prev2.data + carry)
        sum_ = value % 10
        carry = int(value / 10)
        if not new_linked_list:
            head = new_linked_list = Node(sum_)
        else:
            new_node = Node(sum_)
            new_node.next_node = head
            head = new_node
        prev1 = prev1.next_node
        prev2 = prev2.next_node
    if (carry == 1):
        carry_node = Node(carry)
        carry_node.next_node = head
        head = carry_node
    return head

def calculate_length(head):
    start = head
    count = 0
    while(start):
        count += 1
        start = start.next_node
    return count


def append_zeros(head, difference):
    count = 0
    while(count < difference):
        zero_node = Node(0)
        zero_node.next_node = head
        head = zero_node
        count += 1


if __name__ == '__main__':
    head = start = Node(5)
    
    start.next_node = Node(7)
    start = start.next_node

    start.next_node = Node(9)
    start = start.next_node

    head2 = start2 = Node(5)
    
    start2.next_node = Node(4)
    start2 = start2.next_node
    
    start2.next_node = Node(6)
    start2 = start2.next_node

    
    new = add_forward_linked_list(head, head2)
    while(new):
        print(new.data)
        new = new.next_node

