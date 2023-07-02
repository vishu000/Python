class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if temp == None:
            print("linkedlist is empty")
            return
        while temp:
            print(temp.data,"..>",end="")
            temp = temp.next
    
    def enqueue(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
           temp = temp.next
        temp.next = ne
    
    def dequeqe(self):
        temp = self.head
        self.head = temp.next
        temp.next = None


L = Queue()
n1 = Node(5)
L.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
L.display()
