#sample01

class stack:

    def __init__(self):
        self.list = []
    
    def size(self):
        return len(self.list)
    
    def pop(self):
        return self.list.pop()
    
    def push(self, value):
        self.list.append(value)
    
    def printstack(self):
        print(self.list)


a = stack()

str01 = "yesterday"
revstr01 = ""

for char in str01:
    a.push(char)
    
#a.printstack()

while a.size():
    revstr01 = revstr01 + a.pop()

print(revstr01)

str02 = "123456789"

print(sorted(str02, reverse=True))
