class Node:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val


def remove_nth_node(head, n):
    counter = head
    count = 0
    while(counter):
        count += 1
        counter = counter.next
    print(count) 
    index = count - n
    prev = None
    current = head
    count = 0
    while(current):
        if count == index:
            if index == 0:
                print("entered")
                current = current.next
                head = head.next
                print(current.val)
                print(head.val)
            else:
                prev.next = current.next
            break
        prev = current
        current = current.next
        count += 1



#Why isnt head node being deleted. Not undertanding memory management properly
if __name__ == '__main__':
    start = head = Node(val=5)
    head.next = Node(val=7)
    head = head.next
    head.next = Node(val=11)
    head = head.next
    head.next = Node(val=2)
    head = head.next

    remove_nth_node(start, 4)

    while(start):
        print(start.val)
        start = start.next
