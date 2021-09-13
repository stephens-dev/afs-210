class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterateItem(self):
        currentItem = self.head
        while currentItem:
            val = currentItem.data
            currentItem = currentItem.next
            yield val

    def appendItem(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1


items = singlyLinkedList()
items.appendItem('PHP')
items.appendItem('Python')
items.appendItem('C#')
items.appendItem('C++')
items.appendItem('Java')

for val in items.iterateItem():
    print(val)
print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)