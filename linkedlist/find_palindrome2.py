class LinkNode:
    def __init__(self, val):
        self.next = None
        self.val = val



def find_palindrome(head):
    start = fast = slow = head
    while(fast.next):
        fast= fast.next.next
        slow = slow.next

    print("slow is now {}".format(slow.val))
    prev = fast
    current = fast.next
    prev.next = None
    while(current):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        
    while(prev and start):
        if prev.val != start.val:
            return False
        prev = prev.next
        start = start.next
    return True
    #r r r r r r
    # r r





if __name__ == '__main__':

    head = node = LinkNode("r")
    node.next = LinkNode("a")
    node = node.next

    node.next = LinkNode("c")
    node = node.next

    node.next = LinkNode("e")
    node = node.next

    node.next = LinkNode("c")
    node = node.next

    node.next = LinkNode("a")
    node = node.next

    node.next = LinkNode("r")
    noe = node.next 

    print(find_palindrome(head))

