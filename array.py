class Array:
    def __init__(self, length=0):
        self.length = length
        self.data = [None] * length
    
    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value
    
    def insert(self, value):
        for i in range(len(self.data)):
            if self.data[i] == None:
                self.data[i] = value
                return value
        self.data.append(value)
        self.length += 1
        return value
    
    def first_index_of(self, value):
        return self.nth_index_of(value, 1)
    
    def last_index_of(self, value):
        return self.nth_index_of(value, self.length)

    def nth_index_of(self, value, n):
        index = -1
        count = 0
        for i in range(len(self.data)):
            if self.data[i] == value:
                count += 1
                index = i
                if count == n:
                    return index
        return index
    
    def remove_at(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        temp = self.data[index]
        self.data[index] = None
        self.length -= 1
        for i in range(index, self.length):
            self.data[i] = self.data[i + 1]
        self.data[self.length] = None
        return temp

    def pop(self):
        if self.length == 0:
            raise IndexError("Index out of range")
        return self.remove_at(self.length - 1)
    
    def clear(self):
        self.data = [None] * self.length
        self.length = 0
        return self
    
    def copy(self):
        new_array = []
        for i in range(len(self.data)):
            new_array.append(self.data[i])
        return new_array

    def __len__(self):
        return self.length
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def print(self):
        for i in range(len(self.data)):
            if self.data[i] == None:
                return
            elif i != self.length - 1:
                print(self.data[i], end=" ")
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

if __name__ == '__main__':
    a = Array()
    a.insert(1)
    a.insert(2)
    a.print()
    a.insert(3)
    a.insert(8)
    a.insert(4)
    a.insert(5)
    a.insert(8)
    a.insert(6)
    a.insert(8)
    a.insert(7)
    a.insert(8)
    a.print()
    print(a[1])
    print(a.remove_at(1))
    a.print()
    print(len(a))
    print("first index of 8", a.first_index_of(8))
    print("last index of 8", a.last_index_of(8))
    print("second index of 8", a.nth_index_of(8, 2))