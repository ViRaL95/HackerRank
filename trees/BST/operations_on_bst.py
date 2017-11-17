class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    
    def insert(self, data):
        if self.data == data:
            return False

        if self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                new_node = Node()
                new_node.data = data
                self.left = new_node
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                new_node = Node()
                new_node.data = data
                self.right = new_node
                return True
    
    def search(self, data):
        if self.data == data:
            return True
        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    
    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()


    def post_order_traversal(self):
        if self.left:
            return self.left.post_order_traversal()
        if self.right:
            return self.right.post_order_traversal()
        print(self.data)

    #the height of a node is the longest path between itself and a leaf
    def find_height(self, root):
        if not root:
            return -1
        else:
            return max(self.find_height(root.left), self.find_height(root.right)) + 1
    #the depth of a node is the number of edges from the node to the trees root node, root will have 
    #depth of 0
    def find_depth(self, data):
        if self.data == data:
            return 0
        if self.data > data:
            return 1 + self.left.find_depth(data)
        elif self.data < data:
            return 1 + self.right.find_depth(data)

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data


    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    
    def left_view(self):
        if not self:
            return
        print (self.data)
        if self.left:
            print("self left data is %d"%self.left.data)
            return self.left.left_view()
        elif self.right:
            print("self right data is %d"%self.right.data)
            return self.right.left_view()

    def lowest_common_ancestor(self, data1, data2):
        if data1 < self.data and data2 > self.data:
            return self.data
        elif data1 < self.data and data2 < self.data:
            return self.left.lowest_common_ancestor(data1, data2)
        elif data1 > self.data and data2 > self.data:
            return self.right.lowest_common_ancestor(data1, data2)
        
class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        if not self.root:
            print("entered")
            self.root = Node()
            self.root.data = data
        else:
            self.root.insert(data)


    def pre_order_traversal(self):
        self.root.pre_order_traversal()

    def search(self, data):
        if not self.root:
            return False
        self.root.search(data)

    def find_height(self):
        return self.root.find_height(self.root)
    
    def find_depth(self, data):
        return self.root.find_depth(data)
    
    def find_max(self):
        return self.root.find_max()

    def find_min(self):
        return self.root.find_min()

    def left_view(self):
        return self.root.left_view()

    def lowest_common_ancestor(self, data1, data2):
        return self.root.lowest_common_ancestor(data1, data2)

if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(5) # should return false
    tree.insert(7)
    tree.insert(8)
    tree.insert(4)
    tree.insert(2)
    tree.insert(3)
    tree.pre_order_traversal()
    print("height of tree is %d"%tree.find_height())
    print("depth of node 8 is %d"%tree.find_depth(8))
    print(tree.find_max())
    print(tree.find_min())
    print("left view of tree")
    tree.left_view()
    print(tree.lowest_common_ancestor(4, 6))

