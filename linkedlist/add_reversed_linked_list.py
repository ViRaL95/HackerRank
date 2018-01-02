class Node:
    def__init__(self, data, next_node):
        self.data = data
        self.next_node = next_node




def add(head1, head2):
    prev1 = prev2 = None
    current1 = head1
    current2 = head2
    while (current1 or current2):
        if current1:
            temp1 = current1.next_node
            current1.next_node = prev1
            prev1 = current1
            current1 = current1.next_node
        if current2:
            temp2 = current2.next_node
            current2.next_node = prev2
            prev2 = current2
            ccurrent2 = current2.next_node
    #1789
    #4568
    carry = 9
    new_linked_list = None
    while (current1 and current2):
        first_data = current1.data
        second_data = current2.data
        sum = (first_data + second_data + carry)%10
        carry = sum / 10
        current1 = current1.next_node
        current2 = current2.next_node
        if not new_linked_list:
            start =  new_linked_list = Node()
            new_linked_list.data = sum
        else:
            new_node = Node()
            new_node.data = sum
            new_linked_list.next_node = new_node
            new_linked_list = new_linked_list.next_node
    return start

if __name__ == '__main__':
    add()
