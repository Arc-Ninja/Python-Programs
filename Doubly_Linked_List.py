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
        print(f"{data} inserted at beginning")
    def delBeg(self):
        if self.head == None:
            print("Empty LL")
            return
        if self.head.next == None:
            self.head = None
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        print(f"{temp.data} deleted from beginning")
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
        print(f"{data} inserted at end")
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
        print(f"{temp.data} deleted from end")
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
                print(f"{data} inserted at {pos}")
                return
            NN.next = temp
            NN.prev = temp.prev
            temp.prev.next = NN
            temp.prev = NN
        print(f"{data} inserted at {pos}")
    def delPos(self,pos):
        self.pos = pos
        if self.head == None:
            print("Empty List")
            return
        temp = self.head
        if temp.next == None:
            self.head = self.head.next
        elif self.pos == 0:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        else:
            while self.pos > 0 and temp.next != None:
                temp = temp.next
                self.pos -= 1
            if self.pos > 0:
                temp1 = temp.prev
                temp1.next = None
                temp.prev = None
                print(f"{temp.data} Deleted from {pos}")
                return
            elif temp.next == None:
                temp.prev.next = None
                temp.prev = None
                print(f"{temp.data} Deleted from {pos}")
                return
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
        print(f"{temp.data} Deleted from {pos}")

    def disp(self):
        if self.head == None:
            print("Empty LL")
            return
        temp = self.head
        print("\nPrinting . . . \n")
        while temp is not None:
            print("\n",temp.prev)
            print(temp.data)
            print(temp.next,"\n")

            temp = temp.next
        print("\nAll data printed\n")
l = DLL()
l.insBeg(10)
l.insBeg(20)
l.insBeg(30)
l.insBeg(40)
l.insPos(3,35)
l.insEnd(5)
l.insEnd(3)
l.delBeg()
l.delPos(1)
l.delPos(0)
l.insPos(6,69)
l.disp()
