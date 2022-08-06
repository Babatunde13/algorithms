class BinarySearch:
    def __init__(self, data) -> None:
        self.data = data
    
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

a = BinarySearch([1, 2, 4, 5, 6, 7, 8, 8, 9, 10])
print(a.find(10))
