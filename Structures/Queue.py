class Queue():

    def __init__(self, array = []):
        self.queue = array
        self.length = len(array)

    def insert(self , element):
        self.queue.append(element)

    def is_empty(self):
        return self.length == 0

    def deque(self):
        element = self.queue[0]
        self.queue.pop(0)
        return element

