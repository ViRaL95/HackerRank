class Link_Node:
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

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
        """It is very important to know WHEN to use return and when not to use return. 
        In this situation if I do not have an else condition and I simply have no return
        statement under the if condition then this function will only return the root node.
        When a function1 calls itself lets label it function2 recursively and the information returned from function2 needs to be given from function1 to its parent immediately then you are generally
        using return in the correct situation. If for example I remove the return statemnet 
        under the if condition the line of code underneath that line will execute each and every
        time and then return to its parent
        """
        if self.right:
            self.right.find_max()
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

    
    def create_linked_lists(self, depth, hash_map):
        """This method returns n linked lists for all the nodes at each depth
        
        DEPTH OF NODE - Number of edges from the node to the tree's root node

        HEIGHT OF NODE- Number of edges on the longest parth from thee node to a leaf
        """
        if depth not in hash_map:
            hash_map[depth] = Link_Node(self.data)
        else:
            head = hash_map[depth]
            while (head.next_node):
                head = head.next_node
            head.next_node = Link_Node(self.data)
        if self.left:
            self.left.create_linked_lists(depth + 1, hash_map)
        if self.right:
            self.right.create_linked_lists(depth + 1, hash_map)

    def check_if_in_hash_map(self, hash_map, depth, node):
        if depth not in hash_map:
            print("start")
            print("depth %d" %depth)
            hash_map[depth] = node
        else:
            print("yeah")
            head = hash_map[depth]
            while (head.next_node):
                head = head.next_node
            head.next_node = node

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

    def create_linked_list_each_depth(self, hash_map):
        return self.root.create_linked_lists( 0, hash_map)

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
    #tree.pre_order_traversal()
    #print("height of tree is %d"%tree.find_height())
    #print("depth of node 8 is %d"%tree.find_depth(8))
    print(tree.find_max())
    #print(tree.find_min())
    #print("left view of tree")
    #tree.left_view()
    #print(tree.lowest_common_ancestor(4, 6))
    hash_map = {}
    tree.create_linked_list_each_depth(hash_map)
    for key, value in hash_map.items():
        print("depth %d"%key)
        while (value):
            print(value.data)
            value = value.next_node

