class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.start = -1
        self.top = -1
        self.list = [None] * self.max_size

    def __str__(self):
        if self.isEmpty():
            return 'Queue is empty!'
        else:
            if self.top > self.start:
                return ' '.join([str(x) for x in self.list])
            else:
                if self.start > 0:
                    seg_1 = str(self.list[self.start:self.max_size])
                    seg_2 = str(self.list[self.top:self.start])
                    return ' '.join(seg_1) + ' '.join(seg_2)

    def __len__(self):
        counter = 0
        for i in self.list:
            if i is None:
                pass
            else:
                counter += 1
        return counter

    def isEmpty(self):
        if (self.top == -1) and (self.start == -1):
            return True
        return False

    def isFull(self):
        if self.top+1 == self.max_size and self.start == 0:
            return True
        elif (self.start > 0) and self.top + 1 == self.start:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            return 'Queue is full!'
        else:
            if self.top+1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty!'
        else:
            first_item = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start+1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return first_item

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty!'
        else:
            if self.top < self.start:
                value = self.list[self.start]
                return value
            else:
                value = self.list[self.start]
                return value

    def delete(self):
        self.start = -1
        self.top = -1
        self.list = [None] * self.max_size


queue = Queue(max_size=4)
print(queue)
print(len(queue))
print(queue.isEmpty())
print(queue.isFull())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.isFull())
print(queue.enqueue(5))
print(queue.peek())
print(queue.dequeue())
print(len(queue))
print('----')
print(queue)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue)
print(queue.enqueue(55))
print(queue)
print(len(queue))
print(queue.delete())
print(queue)

