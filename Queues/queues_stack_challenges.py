"""Describe how you could use a single Python list to implement three stacks. - Modified this to be multistack"""
class MultiStack:
    def __init__(self, stack_size, n_stack) -> None:
        self.list = [None] * (stack_size * n_stack)
        self.stack_size = stack_size
        self.n_stack = n_stack
    
    def __str__(self) -> str:
        return f"Stack({self.list}, stack_size= {self.stack_size}, n_stack= {self.n_stack})"

    def get_index(self, stack = None):
        if stack:
            a= self.stack_size * stack
            return a - self.stack_size, a

        else: return 0, self.stack_size * self.n_stack

    def is_empty(self, stack= None):
        start, end = self.get_index(stack)
        stack_items= self.list[start : end]
        all_same = all(ele == stack_items[0] for ele in stack_items)
        return  all_same and stack_items[0] == None

        
    def is_full(self, stack = None):
        start, end = self.get_index(stack)
        stack_items= self.list[start : end]
        all_val = all(ele != None for ele in stack_items)
        return all_val
        

    def push(self, value, stack= None):
        assert not self.is_full(stack), 'The stack is full'

        if stack:
            start, end = self.get_index(stack)
            stack_items = self.list[start : end]
            last_none_item_idx= 0
                
            for idx, i in enumerate(stack_items):
                if i == None: 
                    last_none_item_idx= idx
                    break
            self.list[start + last_none_item_idx] = value
        
        else: 
            for idx, i in enumerate(self.list):
                if i == None:
                     self.list[idx] = value
                     break

        return self.list




    def peek(self, stack= None):
        assert not self.is_empty(stack), 'There is no item in the stack'
        
        if stack:
            start, end = self.get_index(stack)
            stack_items = self.list[start : end]

            for i in stack_items:
                if i != None: last_stack_item= i
        
        else: 
            for i in self.list:
                if i != None: last_stack_item= i
        
        return last_stack_item


    def pop(self, stack= None):
        assert not self.is_empty(stack), 'There is no item in the stack'
        
        if stack:
            start, end = self.get_index(stack)
            stack_items = self.list[start : end]

            for idx, i in enumerate(stack_items):
                if i != None:
                    last_stack_item= i
                    last_stack_item_idx= idx
                  
            self.list[start + last_stack_item_idx] = None
            
        
        else: 
            for idx, i in enumerate(self.list):
                if i != None: 
                    last_stack_item= i

                else:
                    self.list[idx -1 ]= None
                    break

        return last_stack_item

    def clear(self, stack =None):
        if stack: 
            start, end = self.get_index(stack)
            self.list[start : end] = [None] * self.stack_size

        else: 
            self.list = [None] * (self.stack_size * self.n_stack)
        
        return self.list
        

# stack=  MultiStack(3, 4)
# print(f"Print: {stack}")
# print(f"is_empty: {stack.is_empty(1)}")
# print(f"is_full: {stack.is_full(2)}")
# print(stack.push(value= 10))
# print(stack.push(value= 20))
# print(stack.push(value= 30))
# print(stack.push(value= 40))
# print(f"Peek: {stack.peek()}")
# print(f"pop: {stack.pop()}")
# print(f"Print: {stack}")
# print(f"Delete: {stack.clear()}")
# print(f"is_empty: {stack.is_empty()}")
# print(f"Print: {stack}")

# stack=  MultiStack(3, 4) # 4 stacks, 3 elements each
# print(f"Print: {stack}")
# print(f"is_empty: {stack.is_empty(1)}")
# print(f"is_full: {stack.is_full(2)}")
# print(stack.push(stack= 1, value= 10))
# print(stack.push(stack= 1, value= 20))
# print(stack.push(stack= 1, value= 30))
# print(stack.push(stack= 2, value= 40))
# print(stack.push(stack= 2, value= 50))
# print(stack.push(stack= 2, value= 60))
# print(stack.push(stack= 3, value= 70))
# print(stack.push(stack= 3, value= 80))
# print(stack.push(stack= 3, value= 90))
# print(f"Print: {stack}")
# print(f"Peek: {stack.peek(3)}")
# print(f"pop: {stack.pop(1)}")
# print(f"Print: {stack}")
# print(f"Delete: {stack.clear(2)}")
# print(f"is_empty: {stack.is_empty(1)}")
# print(f"Print: {stack}")


"""How would you design a stack which, in addition to push and pop, has a function min which 
returns the minimum element? Push, pop and min should all operate in O(1)."""
class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next: Node = next
    
    def __str__(self):
        if self.next:
            return f"Node(value= {self.value}, next= {self.next.value})"
        return f"Node(value= {self.value})"

class Stack:
    def __init__(self):
        self.top = None
        self.mini_node= None
    
    def __str__(self):
        return f"Stack(top= {self.top.value}, min= {self.mini_node.value})"

    def min(self):
        if not self.mini_node: return None
        return self.mini_node.value

    def push(self, value):
        if self.mini_node and (self.mini_node.value < value):
            self.mini_node= Node(value= self.mini_node.value, next= self.mini_node)
        else:
            self.mini_node= Node(value= value, next= self.mini_node)

        self.top= Node(value= value, next= self.top)
        return self.top

    def pop(self):
        if not self.top: return None

        top= self.top
        self.mini_node= self.mini_node.next
        self.top= self.top.next
        return top

# stack= Stack()
# print(f"min: {stack.min()}")
# print(f"push: {stack.push(5)}")
# print(f"min: {stack.min()}")
# print(f"push: {stack.push(5)}")
# print(f"push: {stack.push(3)}")
# print(f"min: {stack.min()}")
# print(f"push: {stack.push(7)}")
# print(f"push: {stack.push(2)}")
# print(f"min: {stack.min()}")
# print(f"Print: {stack}")
# print(f"Pop: {stack.pop()}")
# print(f"Pop: {stack.pop()}")
# print(f"Pop: {stack.pop()}")
# print(f"Pop: {stack.pop()}")
# print(f"Print: {stack}")
# print(f"min: {stack.min()}")
# print(f"Print: {stack}")


"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real 
life, we would likely start a new stack when the previous stack exceeds some threshold. 
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of 
several stacks and should create a new stack once the previous one exceeds capacity, 
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, 
pop() should return the same values as it would if there were just a single stack).

Follow Up: 
Implement a function popAt (int index) which performs a pop operation on a specific sub - stack.
"""