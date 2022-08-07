from time import time

from . import Sort


class BubbleSort(Sort):
    def __init__(self, array) -> None:
        self.array = array

    def sort(self):
        now = time()
        for i in range(0, len(self.array) - 1):
            is_sorted = True
            for j in range(1, len(self.array) - i):
                if self.array[j] < self.array[j - 1]:
                    self.__swap(j, j - 1)
                    is_sorted = False
            if is_sorted:
                print("Took ", time() - now, "s to run")
                return
    
    def __swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp

b = BubbleSort([3, 5, 1, 50, 4, 23, 45, 56, 4, 5, 8, 11, 23, 12, 34, 134, 234, 11, 23, 123, 4, 25, 64])
b.sort()
print(b.array)