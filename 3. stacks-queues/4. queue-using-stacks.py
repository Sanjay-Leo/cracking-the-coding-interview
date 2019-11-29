class Queue:
    def __init__(self):
        self.inbox = []
        self.out = []

    def enqueue(self, value):
        self.inbox.append(value)

    def dequeue(self):
        if len(self.out) == 0:
            while len(self.inbox) != 0:
                self.out.append(self.inbox.pop())
        return self.out.pop()
