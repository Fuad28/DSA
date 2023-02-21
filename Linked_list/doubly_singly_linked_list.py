class Node:
    def __init__(self, value= None) -> None:
        self.value= value
        self.next: Node = None
        self.prev: Node = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class DoublySinglyLinkedList:
    def __init__(self, value) -> None:
        node= Node(value)
        node.prev= None
        node.next= None
        self.head: Node= node
        self.tail: Node= node

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node= node.next
    
    def traverse(self):
        return self.__iter__()
    
    def reverse_traverse(self):
        temp_node= self.tail

        while temp_node:
            print(temp_node.value)
            temp_node= temp_node.prev

    #search is same as singly linked list

    def insert(self, value, location):
        if self.head == None:
            print("Linked list has no node")

        else:
            new_node= Node(value)

            if location == 0:
                new_node.next= self.head
                self.head.prev= new_node
                self.head = new_node 
            
            elif location == -1:
                new_node.prev= self.tail
                self.tail.next = new_node
                self.tail= new_node 

            else:
                temp_node= self.head
                idx= 0

                while idx < location - 1:
                    temp_node= temp_node.next
                    idx += 1
                
                new_node.next= temp_node.next
                new_node.prev= temp_node
                temp_node.next.prev= new_node
                temp_node.next= new_node 


doubly_linked_list= DoublySinglyLinkedList(5)
doubly_linked_list.insert(20, 0)
doubly_linked_list.insert(10, -1)
doubly_linked_list.insert(40, 0)
doubly_linked_list.insert(50, 2)
doubly_linked_list.reverse_traverse()
print([node.value for node in doubly_linked_list.traverse()])
