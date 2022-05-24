from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def put(self,element):
        return self.queue.append(element)

    def get(self):
        return self.queue.popleft() 