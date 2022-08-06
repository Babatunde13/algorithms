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
    
    def contains(self, target):
        if len(self.data_copy) == 0:
            return False
        
        mid_idx = len(self.data_copy) // 2
        mid_value = self.data_copy[mid_idx]
        if target == mid_value:
            return True
        else:
            if target > mid_value:
                self.data_copy = self.data_copy[mid_idx+1:]
                return self.contains(target)
            else:
                self.data_copy = self.data_copy[:mid_idx]
                return self.contains(target)

a = BinarySearch([1, 2, 4, 5, 6, 7, 8, 8, 9, 10])
print(a.find(2))

b = RecursiveBinarySearch([1, 2, 4, 5, 6, 7, 8, 8, 9, 10])
print(b.contains(12))
