import queue


class Queue():
    def __init__(self):
        self.queue = []
        self.front = self.rear = 0
    def queueEnqueue(self,data):
        self.queue.append(data)
        print(f"{data} is pushed")
        self.rear += 1
    def queueDequeue(self):
        if self.rear == 0:
            print("Queue Empty")
        else:
            print(f"{self.queue.pop(0)} is pulled")
            self.rear -= 1
    def queueDisplay(self):
        for _ in self.queue:
            print(_, end="-->")
        print("\n")


q = Queue()
q.queueEnqueue(10)
q.queueEnqueue(20)
q.queueEnqueue(30)
q.queueEnqueue(40)
q.queueDisplay()
q.queueDequeue()
q.queueDequeue()
q.queueDequeue()
q.queueDisplay()
q.queueDequeue()
q.queueDequeue()