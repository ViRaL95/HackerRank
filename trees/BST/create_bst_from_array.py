class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_bst(low, high, array):
    if low == high:
        return TreeNode(array[high])

    if low > high:
        return None

    mid = low + int((high - low)/2)
    root_node = TreeNode(array[mid])
    left_node = create_bst(low, mid - 1, array)
    right_node = create_bst(mid + 1, high, array)
    root_node.left = left_node
    root_node.right = right_node
    return root_node

def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)

if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    root_node = create_bst(0, len(array) - 1, array)
    pre_order(root_node)
    print("-------------")
    array.append(7)
    root_node = create_bst(0, len(array) - 1, array)
    pre_order(root_node)

