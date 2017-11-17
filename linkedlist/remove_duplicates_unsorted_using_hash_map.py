class Node:
    def __init__(self, next_node=None, data=None):
        self.next_node = next_node
        self.data = data

def remove_duplicates(head):
    if not head or not head.next_node:
        return head
    previous = head
    return_node = previous
    hash_map = {}
    hash_map[previous.data] = True
    current = previous.next_node
    while(current):
        if current.data not in hash_map:
            hash_map[current.data] = True
            previous.next_node = current
            previous = previous.next_node
        current = current.next_node
    previous.next_node = None;
    return return_node

if __name__ == '__main__':
    linked_list = None
    start = 0
    while (start < 5):
        end = 0
        while (end < 5):
            if not linked_list:
                head = linked_list = Node()
                linked_list.data = end
            else:
                next_node = Node()
                next_node.data = end
                linked_list.next_node = next_node
                linked_list = linked_list.next_node
            end += 1
        start += 1
    link = remove_duplicates(head)
    while (link):
        print(link.data)
        link = link.next_node

