class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value
    
    def insert(self, value):
        for i in range(len(self.data)):
            if self.data[i] == None:
                self.data[i] = value
                return
        self.data.append(value)
        self.size += 1
    
    def removeAt(self, index):
        temp = self.data[index]
        self.data[index] = None
        self.size -= 1
        for i in range(index, self.size):
            self.data[i] = self.data[i + 1]
        self.data[self.size] = None
        return temp

    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def print(self):
        for i in range(len(self.data)):
            if self.data[i] == None:
                return
            if i != self.size - 1:
                print(self.data[i], end=',')
            else:
                print(self.data[i])

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data
    
    def __add__(self, other):
        return self.data + other.data

    def __iadd__(self, other):
        self.data += other.data
        return self

a = Array(5)
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.print()
print(a[1])
print(a.removeAt(1))
a.print()
print(len(a))