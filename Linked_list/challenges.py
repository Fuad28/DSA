from challenges_linked_list import LinkedList, Node

linked_list = LinkedList()
linked_list.generate(10, 0, 99)
print(linked_list)

def delete_duplicates(linked_list: LinkedList) -> LinkedList:
    if not linked_list.head:
        return

    else:
        current_node= linked_list.head
        visited= set([current_node.value])

        while current_node.next:
            if current_node.next.value in visited:
                current_node.next= current_node.next.next
            else:
                visited.add(current_node.next.value)
                current_node= current_node.next
        
        return linked_list



# delete_duplicates(linked_list)
# print(linked_list)


def nth_to_last_node(linked_list, n):
    if not linked_list.head:
        return
    
    temp_node_1 = linked_list.head
    temp_node_2 = linked_list.head

    for _ in range(n):
        temp_node_2= temp_node_2.next
 
    while temp_node_2:
        temp_node_1= temp_node_1.next
        temp_node_2= temp_node_2.next

    return temp_node_1

# print(nth_to_last_node(linked_list, 4))

# def partition(linked_list, x):
#     """All elements lesser than x should be on the left of x otherwise, they should be on the right"""
#     left, right= Node(), Node()
#     ltail, rtail= left, right

#     curr_node= linked_list.head

#     while curr_node:
#         if curr_node.value > x:
#             ltail.next= curr_node
#             ltail= ltail.next

#         else:
#             rtail.next= curr_node
#             rtail= rtail.next
        
#         curr_node= curr_node.next

        
#     ltail.next= right.next
#     rtail.next= None

#     return left.next


# print(partition(linked_list, 4))


# def sum_list(list_a: LinkedList, list_b: LinkedList):

# def intersection(list_a: LinkedList, list_b: LinkedList)



