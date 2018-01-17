class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def remove_duplicates_two(head):
    if not head:
        return head
    current = head
    while current.next_node:
        prev = current
        third = current.next_node
        while third:
            if third.data != current.data:
                prev.next_node = third
                prev = prev.next_node
            third = third.next_node
        current = current.next_node
        prev.next_node = None
    return head


def remove_duplicates_hashmap(head):
    if not head:
        return head
    hash_map = set()
    prev = head
    current = head.next_node
    while(current):
        if current.data not in hash_map:
            hash_map.add(current.data)
            prev.next_node = current
            prev = prev.next_node
        current = current.next_node
    prev.next_node = None

def print_nodes(head):
    print("--------------------- PRINT NODES ---------------------")
    temp = head
    while temp:
        print (temp.data)
        temp = temp.next_node

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
    start_node.next = Node(5)
    start_node.next.next = Node(5)
    print_nodes(head)
    #remove_duplicates_two(head)
    remove_duplicates_hashmap(head)
    print_nodes(head)
    
