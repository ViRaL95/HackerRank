class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        #if this data already exists within this tree then result falsae
        if self.value == data:
            return False
        #if the data we are trying to insert is less than the current node then 
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        #if the data we are trying to insert is greater than the current node then
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        #find a specific value
        if data == self.value:
            return True
        elif data > self.value:
            if self.rightChild:
                self.rightChild.find(data)
            else:
                return False
        else:
            if self.leftChild:
                self.leftChild.find(data)
            else:
                return False
    #LEFT ROOT RIGHT
    def inorder(self):
        if self:
            if self.leftChild:
                print(self.leftChild.value)
                self.leftChild.inorder()
            print(self.value)
            if self.rightChild:
                print(self.rightChild.value)
                self.rightChild.inorder()
    #LEFT RIGHT ROOT
    def postorder(self):
        if self:
            if self.leftChild:
                print(self.leftChild.value)
                self.leftChild.postorder()
            if self.rightChild:
                print(self.rightChild.value)
                self.rightchild.postorder()
            print(self.value)

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        #if there is atleast one node
        if self.root:
            return self.root.insert(data)
        #if there are no nodes in this tree then insert valueu into tree
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def inorder(self):
        if self.root:
            self.root.inorder()

    def postorder(self):
        if self.root:
            self.root.postorder()


if __name__ == "__main__":
    bst = Tree()
    print(bst.insert(10))
    print(bst.insert(14))
    bst.postorder()
    bst.inorder()

