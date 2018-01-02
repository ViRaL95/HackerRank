class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node 

def create_linked_lists(array):
    new_linked_list = None
    print(array)
    for head in array:
        copy = head
        while(copy):
            if not new_linked_list:
                new = new_linked_list = Node(copy.data)
            else:
                new_node = Node(copy.data)
                new_linked_list.next_node = new_node
                new_linked_list = new_linked_list.next_node
            copy = copy.next_node
    return new


def sort_linked_list(linked_list, low, high):
    if low < high:
        mid = low + int((high - low)/2)
        sort_linked_list(linked_list, low, mid)
        sort_linked_list(linked_list, mid + 1, high)
        merge(linked_list, low, mid, high)


def merge(linked_list, low, mid, high):
    s = left_linked_list = create_mini_linked_list(low, mid, linked_list)
    d = right_linked_list = create_mini_linked_list(mid + 1, high, linked_list)
    counter = 0
    start = head = linked_list
    while(head):
        if counter == low:
            break
        head = head.next_node
        counter += 1
    while(left_linked_list and right_linked_list):
        if left_linked_list.data <= right_linked_list.data:
            head.data = left_linked_list.data
            left_linked_list = left_linked_list.next_node
        else:
            head.data = right_linked_list.data
            right_linked_list = right_linked_list.next_node
        head = head.next_node

    while(left_linked_list):
        head.data = left_linked_list.data
        head = head.next_node
        left_linked_list = left_linked_list.next_node
    while(right_linked_list):
        head.data = right_linked_list.data
        head = head.next_node
        right_linked_list = right_linked_list.next_node
    

def create_mini_linked_list(start, end, linked_list):
    counter = 0
    head = linked_list
    while (head):
        if counter == start:
            finish = new_linked_list = Node()
            new_linked_list.data = head.data
        if counter > start and counter <= end:
            new_node = Node()
            new_node.data = head.data
            new_linked_list.next_node = new_node
            new_linked_list = new_linked_list.next_node
        if counter > end:
            break
        head = head.next_node
        counter += 1
    return finish

def print_linked_list(head):
    print("-------------------")
    start = head
    while (start):
        print(start.data)
        start = start.next_node



def calculate_length(linked_list):
    head = linked_list
    count = 0
    while (head):
        count += 1
        head = head.next_node
    return count

if __name__ == '__main__':
    head = start = Node(5)
    start.next_node = Node(2)
    start = start.next_node

    start.next_node = Node(7)
    start = start.next_node
    
    array = []
    array.append(head)
    
    head2 = start = Node(1)
    start.next_node = Node(3)
    start = start.next_node

    start.next_node = Node(5)
    start = start.next_node
   
    array.append(head2)
     
    head3 = start = Node(-11)
    start.next_node = Node(2)
    start = start.next_node

    start.next_node = Node(8)
    start = start.next_node
    
    start.next_node = Node(4)
    start = start.next_node

    array.append(head3)

    new_linked_list = create_linked_lists(array)
    length = calculate_length(new_linked_list)
    sort_linked_list(new_linked_list, 0 , length - 1)
    while(new_linked_list):
        print(new_linked_list.data)
        new_linked_list = new_linked_list.next_node
  
