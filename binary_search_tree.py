class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value, end=' ')
        if self.right is not None:
            self.right.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

    def inorder(self):
        self.root.inorder()

bst = Tree()

list_of_numbers = input('Enter random numbers: ').split()
list_of_int = []

for number in list_of_numbers:
    list_of_int.append(int(number))

for an_int in list_of_int:
    bst.add(an_int)

print('Your list has been sorted: ', end=' ')
bst.inorder()