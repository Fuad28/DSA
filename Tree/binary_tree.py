class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __str__(self) -> str:
        return str(self.data)

new_Btree= TreeNode("Drinks")
hot= TreeNode("Hot")
cold= TreeNode("Cold")
new_Btree.left_child = hot
new_Btree.right_child = cold

tea= TreeNode("Tea")
coffee= TreeNode("Coffee")
hot.left_child = tea
hot.right_child = coffee

fanta= TreeNode("Fanta")
coke= TreeNode("Coke")
cold.left_child = fanta
cold.right_child = coke



def preorder_traversal(root_node):
    if not root_node:
        return

    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)

# preorder_traversal(new_Btree)


def inorder_traversal(root_node):
    if not root_node:
        return

    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)

# inorder_traversal(new_Btree)


def postorder_traversal(root_node):
    if not root_node:
        return

    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.data)
    
# postorder_traversal(new_Btree)

# We need Queue to implement this.
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' -> '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        return self.linkedList.head == None
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
        

def levelorder_traversal(root_node):
    if not root_node:
        return

    queue = Queue()
    queue.enqueue(root_node)

    while not queue.isEmpty():
        root = queue.dequeue()
        print(root.value.data)

        if root.value.left_child is not None:
            queue.enqueue(root.value.left_child)

        if root.value.right_child is not None:
            queue.enqueue(root.value.right_child)

    

levelorder_traversal(new_Btree)