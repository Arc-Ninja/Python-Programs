class node:
    def __init__(self,val):
        self.data = val
        self.link = None

class Stack:
    def __init__(self):
        self.head = None
        print("Stack created")
    def push(self,val):
        nn = node(val)
        if self.head == None:
            self.head = nn
        else:
            nn.link = self.head
            self.head = nn
        print(f"{val} is pushed")
    def pull(self):
        if self.head == None:
            print("Stack empty")
        else:
            temp = self.head
            self.head = self.head.link
            temp.link = None
    def peek(self):
        if self.head == None:
            print("Stack empty")
        else:
            print(self.head.data)
    def printStack(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.link

s1 = Stack()
s1.push(24)
s1.push(25)
s1.push(26)
s1.printStack()
s1.peek()
s1.pull()
s1.pull()
s1.peek()
s1.pull()
s1.pull()
s1.peek()