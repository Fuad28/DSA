"""
# Bear in mind that, head and tail are basically the first and last nodes only that they get the head and tail designations.
#So a Linked list with one node has the single node as its head and tail


1. There's a head
2. There's a tail.
3. Each Node contains data and a ref to the next node
4. Head Node contains the designation of head and ref to the next node (it doesn't contain data)
5. Last node (before tail node) contains data and null for its ref part (It contains data but no ref)
6. Tail node contains data and  ref to the last node (It contains data and ref)
7. Head, first, last and tail nodes are different.

Comparison with arrays
1. Each node in a linked list is an independent object that can be deleted unlike arrays that deleting an element still retains it's cell (i.e memory space)
2. Insertion in linked list isn't like in arrays that other elements have to be moved
3. To access an item, you've to traverse through the linked list

Types
1. Singly linked list: The one explained baove
2. Circular singly linked list: The last node has a ref to the first node
3. Doubly linked list: Similar to single linked list except that each node has a ref to the previous node and a ref to the next node.
4. Circular doubly linked list: 


"""

class Node:
    def __init__(self, value= None) -> None:
        self.value= value
        self.next: Node = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node= None
        self.tail: Node= None

    def __iter__(self):
        node= self.head
        while node:
            yield node # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
            node= node.next

    def insert(self, value, location):
        new_node= Node(value)

        if self.head is None:
            self.head= new_node
            self.tail= new_node

        else:
            if location == 0: #insert element at the beginning of linked list
                new_node.next= self.head
                self.head= new_node
            
            elif location == -1:
                temp_node= self.tail
                temp_node.next= new_node
                self.tail= new_node

            else:
                prev_node= self.head
                index= 0

                while index < location - 1: # this iteration stops an index before the specified location 
                    prev_node= prev_node.next
                    index+= 1
                
                next_node= prev_node.next
                prev_node.next= new_node
                new_node.next= next_node

                if prev_node == self.tail:
                    self.tail= new_node

    def traverse(self):
        return self.__iter__()

    def search(self, value):
        if temp_node:= self.head: #walrus
            while temp_node.next !=  None:
                if temp_node.value == value: 
                    return f"{temp_node}"
                
                temp_node= temp_node.next
            return f"Node with value {value} does not exist"

        return "Linked list has no value"

    
    def delete(self, location):
        if not self.head: return "Linked list has no node"

        assert type(location) == int, "location of node must be of type integer"

        len_linked_list= len([node.value for node in self])

        assert location <= len_linked_list, f"location is out of bounds for linked list of size {len_linked_list}"


        if len_linked_list == 1:
                self.head= None
                self.tail= None
        
        else:

            if location == 0:
                self.head = self.head.next
                    
            
            elif location == -1:
                before_last= self.head
                idx= 0

                while idx < len_linked_list -2:
                    before_last= before_last.next
                    idx += 1

                before_last.next= None
                self.tail= before_last

            else:
                prev_node= self.head
                idx= 0

                while idx < location -1:
                    prev_node= prev_node.next
                    idx += 1
            
                if prev_node.next.next:
                    next_node= prev_node.next.next
                    prev_node.next= next_node
                    
                else:
                    prev_node.next= None
    
    def delete_all(self):
        if not self.head: print("Linked list has no node")
        else:
            self.head= None
            self.tail= None

            




slinked_list1= SinglyLinkedList()
node1= Node(1)
node2= Node(2)
slinked_list1.head= node1
slinked_list1.head.next= node2
slinked_list1.tail= node2
# print([node.value for node in slinked_list1])

slinked_list1.insert(3, 0) #insert at the beginning
slinked_list1.insert(4, -1) #insert at the the end
slinked_list1.insert(5, 3) #insert at an index

#traversing
# print([node.value for node in slinked_list1])
# print([node.value for node in slinked_list1.traverse()])

#searching
# print(slinked_list1.search(5))

#deletion
# print([node.value for node in slinked_list1])
# slinked_list1.delete(-1) #delete at an index
# slinked_list1.delete(0) #delete at the beginning
# slinked_list1.delete(-1) #delete at the the end
# slinked_list1.delete_all() #delete entire linked list




