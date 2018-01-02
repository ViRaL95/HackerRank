class Node:
    def __init__(self, next_node=None, data=None):
        self.next_node = next_node
        self.data = data


def detect_cycle_no_space_complexity(head):
    if not head or not head.next_node:
        return head
    slow = fast = head
    while (fast and fast.next_node):
        fast = fast.next_node.next_node
        slow = slow.next_node
        if not fast:
            return False
        if fast is slow:
            return True
    #if fast points to the last node that means that there is no next. We have to check however
    #that fast and slow dont point to the same node. If it does then return True otherwise return 
    # False
    #if fast is slow:
    #    return True
    return False













if __name__ == '__main__':
    pointer1 = head = Node()
    head.data = 7
    
    next_node = Node()
    next_node.data = 8
    head.next_node = next_node
    head = head.next_node

    next_node = Node()
    next_node.data = 9
    head.next_node = next_node
    head = head.next_node

    head.next_node = pointer1
    
    print(detect_cycle_no_space_complexity(pointer1))
    
    pointer1 = head = Node()
    head.data = 7
    
    next_node = Node()
    next_node.data = 8
    head.next_node = next_node
    head = head.next_node

    next_node = Node()
    next_node.data = 9
    head.next_node = next_node
    head = head.next_node

    print(detect_cycle_no_space_complexity(pointer1))

    next_node = Node()
    next_node.data = 10
    head.next_node = next_node
    head = head.next_node

    head.next_node = pointer1
    head = head.next_node

    print(detect_cycle_no_space_complexity(pointer1))
