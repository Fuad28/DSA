class Node:
    def __init__(self, value=None):
        self.value = value
        self.next: Node = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head: Node = None
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next



class Stack:
    def __init__(self, linked_list):
        self.list= linked_list

    def __str__(self):
        return self.list.__str__()

    def peek(self):
        assert self.is_empty, 'There is no item in the stack'
        return self.list.head

    def pop(self):
        assert self.is_empty, 'There is no item in the stack'
        popped= self.list.head
        self.list.head= self.list.head.next
        return popped

    def push(self, value):
        new_node= Node(value)
        new_node.next= self.list.head
        self.list.head= new_node
        return "Element succesfully inserted"

    def delete(self):
        self.list.head = None
        return "Stack emptied"
    
    @property
    def is_empty(self):
        return True if not self.list.head else False


linked_list= LinkedList()
stack= Stack(linked_list)

print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(f"is_empty: {stack.is_empty}")
print(stack.push(40))
print(f"Peek: {stack.peek()}")
print(f"Print: {stack}")
print(f"Pop: {stack.pop()}")
print(f"Print: {stack}")
print(f"Delete: {stack.delete()}")
print(f"is_empty: {stack.is_empty}")
print(f"Print: {stack}")