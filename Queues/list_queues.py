#Queues work on FIFO


class Queue:
    def __init__(self, max_cap= 0):
        self.list= []
        self.max_cap= max_cap

    def __str__(self):
        values= self.list.copy()
        values.reverse()
        values= [str(x) for x in values]
        return "->".join(values)

    def peek(self):
        assert not self.is_empty, 'There is no item in the queue'
        return self.list[0]

    def dequeue(self):
        assert not self.is_empty, 'There is no item in the queue'
        return self.list.pop(0)

    def enqueue(self, value):
        assert not self.is_full, 'The queue is full'
        self.list.append(value)
        return "Element succesfully inserted"

    def delete(self):
        self.list= []
        return "Queue emptied"
    
    @property
    def is_empty(self):
        return True if not len(self.list) else False

    @property
    def is_full(self):
        return len(self.list) >= self.max_cap


queue= Queue(10)
print(queue.enqueue(10))
print(queue.enqueue(20))
print(queue.enqueue(30))
print(f"is_empty: {queue.is_empty}")
print(f"is_full: {queue.is_full}")
print(queue.enqueue(40))
print(f"Peek: {queue.peek()}")
print(f"Print: {queue}")
print(f"dequeue: {queue.dequeue()}")
print(f"Print: {queue}")
print(f"Delete: {queue.delete()}")
print(f"is_empty: {queue.is_empty}")
print(f"Print: {queue}")