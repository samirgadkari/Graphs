class Queue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        res = ''
        for v in self.queue:
            res += str(v) + '...'
        print('self.size:', self.size())
        return res

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
