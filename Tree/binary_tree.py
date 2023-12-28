class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child: TreeNode = None
        self.right_child: TreeNode = None

    def __str__(self, level=0):
        result = ""
        if self.left_child:
            result += self.left_child.__str__(level + 1)
        result += "\n" + ("    " * level) + str(self.data)
        if self.right_child:
            result += self.right_child.__str__(level + 1)
        return result


new_Btree = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
new_Btree.left_child = hot
new_Btree.right_child = cold

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.left_child = tea
hot.right_child = coffee

fanta = TreeNode("Fanta")
coke = TreeNode("Coke")
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

# We need Queue to implement level order traversal. So we use a linked list based queue.


class LinkedList:
    def __init__(self):
        self.head: TreeNode = None
        self.tail: TreeNode = None


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def enqueue(self, value):

        new_node = TreeNode(value)
        if self.linkedList.head == None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def isEmpty(self):
        return self.linkedList.head == None

    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            currhead = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = currhead.next
            return currhead


def levelorder_traversal(root_node):
    if not root_node:
        return

    queue = Queue()
    queue.enqueue(root_node)

    while not queue.isEmpty():
        root = queue.dequeue()
        print(root.value.data)

        if root.value.left_child is not None:
            queue.enqueue(root.left_child)

        if root.value.right_child is not None:
            queue.enqueue(root.right_child)

    return root  # root will be the last node
# levelorder_traversal(new_Btree)


# searching for an element of the queue
# we use levelorder traversal because it uses a queue since queue performs better than stack kjhvjkdshkjdshkdjshkjdshvklxjbvjkdsnbsdkjbhfsdjkbfjkhbkdjfmhvjkdfbndhj
def search_tree(root_node, value):
    if not root_node or not value:
        return

    queue = Queue()
    queue.enqueue(root_node)

    while not queue.isEmpty():
        root = queue.dequeue()

        if value == root.value.data:
            print(f"Node found: {root.data}")
            return root

        if root.left_child is not None:
            queue.enqueue(root.left_child)

        if root.value.right_child is not None:
            queue.enqueue(root.right_child)

    print(f"Node not found")
    return


# search_tree(new_Btree, "Hot")


def insert_node(root_node, value):
    if not root_node or not value:
        return

    new_node = TreeNode(value)

    queue = Queue()
    queue.enqueue(root_node)

    while not queue.isEmpty():
        root = queue.dequeue()

        if root.left_child is not None:
            queue.enqueue(root.left_child)

        else:
            root.left_child = new_node

        if root.right_child is not None:
            queue.enqueue(root.right_child)

        else:
            root.right_child = new_node

    return root_node


# tree = insert_node(new_Btree, "Nutri Choco")
# print(tree)

# This is done by replacing the node to be deleted by the deepest node (the last node that'll be reached during level order traversal)
# and deleting the deepest node from its original location.

def get_deepest_node(root_node):
    if not root_node:
        return

    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if (root.left_child is not None):
                custom_queue.enqueue(root.left_child)

            if (root.right_child is not None):
                custom_queue.enqueue(root.right_child)

        return root.data


def delete_deepest_node(root_node, d_node):
    if not root_node:
        return

    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()

            if root.data is d_node:
                root.data = None
                root.left_child = None
                root.right_child = None

                return

            if root.right_child:

                if root.right_child is d_node:
                    root.right_child = None
                    return

                else:
                    custom_queue.enqueue(root.right_child)

            if root.left_child:

                if root.left_child is d_node:
                    root.left_child = None
                    return

                else:
                    custom_queue.enqueue(root.left_child)


def delete_node_bT(root_node, node):
    if not root_node:
        return "The BT does not exist"

    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()

            if root.data == node:
                d_node: TreeNode = get_deepest_node(root_node)
                root.data = d_node.data
                delete_deepest_node(root_node, d_node)
                return "The node has been successfully deleted"

            if (root.left_child is not None):
                custom_queue.enqueue(root.left_child)

            if (root.right_child is not None):
                custom_queue.enqueue(root.right_child)
        return "Failed to delete"


def delete_bT(root_node: TreeNode):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BT has been successfully deleted"
