class TreeNode:
    def __init__(self, data, children: list = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0) -> str:
        ret = " " * level + str(self.data) + "\n"

        for child in self.children:
            ret += child.__str__(level+ 1)

        return ret
    
    def add_child(self, tree_node):
        assert isinstance(tree_node, TreeNode), "Child has to be of type TreeNode"
        self.children.append(tree_node)


tree = TreeNode("Drinks", [])

cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tree.add_child(cold)
tree.add_child(hot)

coke = TreeNode("Coke", [])
fanta = TreeNode("Fanta", [])
cold.add_child(coke)
cold.add_child(fanta)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
hot.add_child(tea)
hot.add_child(coffee)


print(tree)