class Link_Node:
        
        def __init__(self, data=None, next_node=None, prev_node=None):
            self.data = data
            self.next_node = next_node
            self.prev_node = prev_node
        

class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
        self.max_top = None
    
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


    def find_height_wo(self):
        """Find height of tree without passing root as parameter to function.

        """ 
        if not (self.left or self.right):
            return 0
        if not self.left:
            return 1 + max(0, self.right.find_height_wo())
        if not self.right:
            return 1 + max(self.left.find_height_wo(), 0)
        return 1 + max(self.left.find_height_wo(), self.right.find_height_wo())
        
 
    #depth of a node is the number of nodes from the root node
    #for each 
    def find_depth(self, data, depth):
        if self.data == data:
            return depth
        if self.data > data:
            return self.left.find_depth(data, depth + 1)
        if self.data < data:
            return self.right.find_depth(data, depth + 1)


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

    def create_doubly_linkedlist(self, prev_node):
        if self.left:
            self.left.create_doubly_linked_list(prev_node)
        global prev


        try:
            prev
        except NameError:
            prev = prev_node
        new_node = Link_Node(self.data)
        prev.next_node = new_node
        new_node.prev_node = prev
        prev = new_node

        if self.right:
            self.right.create_doubly_linked_list(prev_node)

    
    def find_distance_between_nodes(self, data1, data2):
        if self.data < data1 and self.data < data2:
            return self.right.find_distance_between_nodes(data1, data2)
        
        if self.data > data1 and self.data > data2:
            return self.left.find_distance_between_nodes(data1, data2)

        if self.data >= data1 and self.data <= data2:
            return self.find_height(data1) + self.find_height(data2)



    def find_height(self, data):
        if self.data == data:
            return 0

        if self.data > data:
            return 1 + self.left.find_height(data)

        if self.data < data:
            return 1 + self.right.find_height(data)

    def delete_leaves(self):
        """ This function will delete all leaves from a tree, but if the root is the only
        node given it will not delete itself
        """
        if not (self.left or self.right):
            return True
        if self.left:
            delete = self.left.delete_leaves()
            if delete is True:
                self.left = None
        if self.right:
            delete = self.right.delete_leaves()
            if delete is True:
                self.right = None

    def delete_leaves_2(self, root):
        """ This functino will delete all leaves from  tree including the original

        """
        if not (root.left or root.right):
            print("delete")
            print(root.data)
            print("---------")
            root = None
            return

        if root.left:
            self.delete_leaves_2(root.left)

        if root.right:
            self.delete_leaves_2(root.right)


class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        if not self.root:
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

    def find_height_wo(self):
        return self.root.find_height_wo()

    
    def create_doubly_linked_list(self, node):
        return self.root.create_doubly_linked_list(node)

    
    def find_distance_between_nodes(self, data1, data2):
        return self.root.find_distance_between_nodes(data1, data2)
       
    def delete_leaves(self):
        self.root.delete_leaves()
    
    def delete_leaves_2(self):
        self.root.delete_leaves_2(self.root)

    def find_depth(self, data, depth):
        return self.root.find_depth(data, depth)
     
    def find_max_path(self):
        find_max_path.max_top = float("-inf")
        find_max_path(self.root)
        return find_max_path.max_top

    def find_sum(self):
        find_sub_sum.sum_path = 0
        find_sum(self.root, 12)

    def create_linked_list

def find_max_path(root):
    if not root:
        return 0
    left = find_max_path(root.left)
    right = find_max_path(root.right)
    left_right_root = max(max(left, right) + root.data, root.data)
    left_right_root_subtree = max(left_right_root, left + right + root.data)
    find_max_path.max_top = max(find_max_path.max_top, left_right_root_subtree)
    return left_right_root


def find_sum(root, sum_):
    if not root:
        return
    find_sum(root.left, sum_)
    find_sum(root.right, sum_)
    print("-----------------")
    find_sub_sum(root, sum_)


def find_sub_sum(root, sum_):
    if not root:
        return
    print(root.data)
    if sum_ - root.data ==  0:
        print("entered for root value of %d",root.data)
        find_sub_sum.sum_path += 1
    find_sub_sum(root.left, sum_ - root.data)
    find_sub_sum(root.right, sum_ - root.data)




if __name__ == '__main__':
    tree = Tree()
    tree.insert(12)
    tree.insert(13)
    tree.insert(14)
    tree.insert(15)
    tree.insert(4)
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(8)
    #print(tree.find_height_wo())
    #print(tree.find_height_again())
    #tree.pre_order_traversal()
    #print("height of tree is %d"%tree.find_height())
    #print("depth of node 8 is %d"%tree.find_depth(8))
    #print(tree.find_max())
    #print(tree.find_min())
    #print("left view of tree")
    #tree.left_view()
    #print(tree.lowest_common_ancestor(4, 6))
    #hash_map = {}
    #tree.create_linked_list_each_depth(hash_map)
    """for key, value in hash_map.items():
        print("depth %d"%key)
        while (value):
            print(value.data)
            value = value.next_node"""
    print("-------------------")
    '''node = Link_Node()
    tree.create_doubly_linked_list(node)
    while (node):
        print(node.data)
        node = node.next_node
    print(tree.find_distance_between_nodes(13, 15))'''
    #tree.delete_leaves()
    #print(tree.find_depth(15, 0))
    #tree.delete_leaves_2()
    #tree.pre_order_traversal()
    #print(tree.find_max_path())
    tree.find_sum()
    print(find_sub_sum.sum_path)
    tree.create_linked_list_depth()
    #12 is the root. 12 is one value
