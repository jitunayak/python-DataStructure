class stack():
    def __init__(self):
        self.items= []

    def push(self,item):
        if item==' ':
            print("Empty data inserted")
            return False
        else:    
            self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getStack(self):
        return self.items
    def isEmpty(self):
        return self.items ==[]

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]   

# s= stack()
# s.push(" ")
# s.push(" ")
# s.push(" ")

# print(s.getStack())
# s.pop()
# print(s.getStack())
# print(s.isEmpty())
# print(s.peek())
# s.pop()
# s.pop()
# print(s.isEmpty())
# print(s.peek)


