class TreeNode:
    def __init__(self, right=None, left=None, val=None):
        self.right = right
        self.left = left
        self.val = val


class LinkNode:
    def __init__(self, val=None, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.val = val


def tree_to_doubly(root):
    if not root:
        return    
    tree_to_doubly(root.left)

    new_node = LinkNode(val=root.val)
    new_node.prev = tree_to_doubly.current
    tree_to_doubly.current.next = new_node
    tree_to_doubly.current = tree_to_doubly.current.next

    tree_to_doubly(root.right)

if __name__ == '__main__':
    root = TreeNode(val=9)
    root.right = TreeNode(val=7)
    root.left = TreeNode(val=6)
    root.right.right = TreeNode(val=30)
    root.right.left = TreeNode(val =2)
    root.left.left = TreeNode(val=17)
    root.left.left.left = TreeNode(val=12)
    
    dummy_node = LinkNode()
    tree_to_doubly.current = dummy_node

    tree_to_doubly(root)

    print("--------------NEXT--------")
    while(dummy_node.next):
        print(dummy_node.val)
        dummy_node = dummy_node.next
    print(dummy_node.val)
    print("------------ PREV---------")
    while(dummy_node.prev):
        print(dummy_node.val)
        dummy_node = dummy_node.prev

