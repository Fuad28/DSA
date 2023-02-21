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

stack=  MultiStack(3, 4) # 4 stacks, 3 elements each
print(f"Print: {stack}")
print(f"is_empty: {stack.is_empty(1)}")
print(f"is_full: {stack.is_full(2)}")
print(stack.push(stack= 1, value= 10))
print(stack.push(stack= 1, value= 20))
print(stack.push(stack= 1, value= 30))
# print(stack.push(stack= 1, value= 40))
print(f"Peek: {stack.peek(1)}")
print(f"pop: {stack.pop(1)}")
print(f"Print: {stack}")
print(f"Delete: {stack.clear(2)}")
print(f"is_empty: {stack.is_empty(1)}")
print(f"Print: {stack}")

