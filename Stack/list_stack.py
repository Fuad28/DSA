#Queues work on LIFO

class Stack:
    def __init__(self):
        self.list= []

    def __str__(self):
        values= self.list.copy()
        values.reverse()
        values= [str(x) for x in values]
        return "\n".join(values)

    def peek(self):
        assert len(self.list) > 0, 'There is no item in the stack'
        return self.list[-1]

    def pop(self):
        assert len(self.list) > 0, 'There is no item in the stack'
        return self.list.pop()

    def push(self, value):
        self.list.append(value)
        return "Element succesfully inserted"

    def delete(self):
        self.list= []
        return "Stack emptied"
    
    @property
    def is_empty(self):
        return True if not len(self.list) else False


stack= Stack()
# print(stack.peek())
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(stack.push(40))
print(stack.peek())
print(stack.pop())
print("\n")
print(stack)

#task. implement max size concept