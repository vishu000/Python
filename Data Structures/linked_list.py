class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singleLL:
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
    
    def insert_begin(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
           temp = temp.next
        temp.next = ne
    
    def delete_begin(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next:
            temp = temp.next
            prev = prev.next
        prev.next = None


L = singleLL()
n1 = Node(5)
L.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
L.insert_begin(1)
L.insert_end(20)
L.delete_begin()
L.delete_end()
L.display()
