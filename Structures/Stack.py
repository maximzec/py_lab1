class Stack():

    def __init__(self, array=[]):
        self.stack = array

    def pop(self):
           return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return self.stack == []

    def clear(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def __str__(self):
        out = ""
        for num in self.stack:
            out += str(num)+" "
        return out
