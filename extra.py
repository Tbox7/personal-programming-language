class Stack:
    def __init__(self):
        self.wtf = []
    def push(self, value):
        self.wtf.append(value)
    def pop(self):
        self.wtf.remove(self.wtf[0])
    def peek(self):
        print(self.wtf[0])
new_list = Stack()
new_list.push(1)
new_list.push(2)
new_list.push(3)
new_list.push(4)
new_list.push(5)
print(new_list.wtf)
new_list.pop()
print(new_list.wtf)
new_list.peek()

