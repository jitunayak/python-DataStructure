
class queue:
    
    def __init__(self):
        self.items = [None]*4
        self.front = self.rear =-1

    def add(self,item):
        if self.front==3:
            self.front = 0
            self.items[self.front]=item

        self.front += 1    
        self.items[self.front]=item

    def remove(self):
        return self.items.pop(0)

    def show(self):
        return self.items


def main():
    q= queue()
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    print(q.show())
    q.remove()    
    print(q.show())
    q.remove()
    q.add(3)
    q.add(4)
    q.add(5)    
    print(q.show())
    q.remove()    
    print(q.show())
main()