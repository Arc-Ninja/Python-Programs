class node:
    def __init__(self,data):
        self.data = data
        self.link = None
class Queue:
    def __init__(self):
        self.front = self.rear =None
    def enqueue(self,data):
        temp = node(data)
        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.link = temp
            self.rear = temp
    def dequeue(self):
        if self.front==None:
            print("Queue Empty")
        else:
            temp = self.front
            self.front = temp.link
            if self.front == None:
                self.rear = None
    def disQueue(self):
        if self.front==None:
            print("Queue Empty")
        else:
            print(self.front.data)
                
        
a = Queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.enqueue(40)
a.dequeue()
a.disQueue()
a.dequeue()
a.disQueue()
a.dequeue()
a.dequeue()
a.dequeue()
a.disQueue()