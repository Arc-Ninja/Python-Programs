class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def insBeg(self,data):
        NN = node(data)
        if self.head == None:
            self.head = NN
            return
        NN.next = self.head
        self.head.prev = NN
        self.head = NN
    def delBeg(self):
        if self.head == None:
            print("Empty LL")
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
    def insEnd(self,data):
        NN = node(data)
        if self.head == None:
            self.head = NN
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = NN
        NN.prev = temp
    def delEnd(self):
        if self.head == None:
            print("Empty LL")
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp1 = temp.next
        temp.next = None
        temp1.prev = None
    def insPos(self,pos,data):
        self.pos = pos
        NN = node(data)
        if self.head == None:
            self.head = NN
            print(f"LL was empty so {data} has been inserted in first position")
            return
        temp = self.head
        if self.pos==0:
            NN.next = self.head
            self.head.prev = NN
            self.head = NN
        else:
            while self.pos > 0 and temp.next != None:
                temp = temp.next
                self.pos -= 1
            if self.pos>0:
                temp.next = NN
                NN.prev = temp
                return
            NN.next = temp
            temp1 = temp.prev
            temp.prev = NN
            temp1.next = NN
    def disp(self):
        if self.head == None:
            print("Empty LL")
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
l = DLL()
l.insBeg(10)
l.insBeg(20)
l.disp()
