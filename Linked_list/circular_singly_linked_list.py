class Node:
    def __init__(self, value= None) -> None:
        self.value= value
        self.next: Node = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class CircularSinglyLinkedList:
    def __init__(self, value) -> None:
        node= Node(value)
        node.next= node
        self.head: Node= node
        self.tail: Node= node

    
    def insert(self, value, location):
        assert type(location) == int, "Location parameter can only be integers"

        new_node= Node(value)

        if location == 0:
            new_node.next= self.head
            self.head= new_node
            self.tail.next= new_node
        
        elif location == -1:
            self.tail.next= new_node
            new_node.next= self.head
            self.tail= new_node
        
        else:
            temp_node= self.head
            idx= 0

            while idx < location -1:
                temp_node= temp_node.next
                idx += 1

            next_node= temp_node.next
            temp_node.next= new_node
            new_node.next= next_node

    
    def traverse(self):
        return self.__iter__()

    def search(self, value):
        if temp_node:= self.head:
            while temp_node.next !=  self.head:
                if temp_node.value == value: 
                    return f"{temp_node}"
                
                temp_node= temp_node.next
            return f"Node with value {value} does not exist"

        return "Linked list has no value"

    def delete(self, location):
        if self.head == None:
            print("There is no node in the linked list")

        else:
            if location == 0:
                if self.head == self.tail: #only one node
                    self.head = self.head.next = self.tail= None
                
                else:
                    self.head= self.head.next
                    self.tail.next = self.head
            
            elif location == -1:
                if self.head == self.tail: #only one node
                    self.head= self.head.next = self.tail= None
                
                else:
                    temp_node = self.head

                    while temp_node is not None:
                        if temp_node.next == self.tail:
                            break
                        temp_node= temp_node.next

                    temp_node.next= self.head
                    self.tail= temp_node
            
            else:
                temp_node = self.head
                idx= 0

                while idx < location - 1:
                    temp_node= temp_node.next
                    idx += 1

                temp_node.next= temp_node.next.next
        
    def delete_all(self):
        self.head= None
        self.tail.next= None
        self.tail= None


                    



                    


    def __iter__(self):
        node= self.head
        while node:
            yield node 
            node= node.next
            if node == self.tail.next: 
                break


circular_linked_list= CircularSinglyLinkedList(1)
circular_linked_list.insert(20, 0)
circular_linked_list.insert(10, -1)
circular_linked_list.insert(40, 0)
circular_linked_list.insert(50, 2)
print(circular_linked_list.search(40))
print(circular_linked_list.search(100))
print([node.value for node in circular_linked_list.traverse()])
circular_linked_list.delete_all()
print([node.value for node in circular_linked_list.traverse()])
