class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.isEmpty():
            return 'queue is empty!'
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            counter = 0
            for i in self.list:
                counter += 1
            return counter

    def enqueue(self, value):
        self.list.append(value)
        return 'value enqueued!'

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty!'
        return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty!'
        return self.list[0]

    def delete(self):
        self.list = []
        return 'Queue was deleted!'


queue = Queue()
print(queue.isEmpty())
print(len(queue))
print(queue.enqueue(1))
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.isEmpty())
print(queue)
print(len(queue))
print(queue.peek())
print(queue.dequeue())
print(queue)
print(len(queue))
queue.delete()
print(queue)
print(len(queue))