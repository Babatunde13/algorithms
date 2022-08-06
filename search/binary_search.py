class BinarySearch:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0
    
    def find(self, target):
        first = 0
        last = len(self.data) - 1
        while first <= last:
            mid_idx = (last + first) // 2
            mid_value = self.data[mid_idx]
            if target == mid_value:
                return mid_idx
            elif target > mid_value:
                first = mid_idx + 1
            else:
                last = mid_idx - 1
        return -1

class RecursiveBinarySearch:
    def __init__(self, data) -> None:
        self.data = data
        self.data_copy = data
        self.index = 0
    
    def find(self, target):
        if len(self.data_copy) == 0:
            return -1
        
        mid_idx = len(self.data_copy) // 2
        self.index += mid_idx
        mid_value = self.data_copy[mid_idx]
        if target == mid_value:
            return self.index
        else:
            if target > mid_value:
                self.data_copy = self.data_copy[mid_idx:]
                return self.find(target)
            else:
                self.data_copy = self.data_copy[:mid_idx]
                return self.find(target)

a = BinarySearch([1, 2, 4, 5, 6, 7, 8, 8, 9, 10])
print(a.find(10))

b = RecursiveBinarySearch([1, 2, 4, 5, 6, 7, 8, 8, 9, 10])
print(b.find(10))
