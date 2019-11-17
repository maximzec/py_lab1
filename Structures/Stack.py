class Stack():

    def __init__(self, array=[]):
        self.length = len(array)
        self.stack = array

    def pop(self):
        if self.length != 0:
            self.stack.pop(len(self.stack) - 1)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def push(self, element):
        self.stack.append(element)

    def clear(self):
        self.stack = []

