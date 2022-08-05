class BubbleSort:
    def __init__(self, array) -> None:
        self.array = array

    def sort(self):
        for i in range(0, len(self.array) - 1):
            is_sorted = True
            for j in range(1, len(self.array) - i):
                if self.array[j] < self.array[j - 1]:
                    self._swap(j, j - 1)
                    is_sorted = False
            if is_sorted:
                return
    
    def _swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp
