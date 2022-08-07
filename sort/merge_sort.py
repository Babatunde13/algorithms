from time import time

class MergeSort:
    def __init__(self, data) -> None:
        self.data = data
    
    def __swap(self, index1, index2):
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp
    
    def __split(self, data):
        midpoint = len(data) // 2
        array1 = data[:midpoint]
        array2 = data[midpoint:]
        return array1, array2

    def __merge(self, left, right):
        array = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array.append(left[i])
                i += 1
            else:
                array.append(right[j])
                j += 1
        while i < len(left):
            array.append(left[i])
            i += 1
        while j < len(right):
            array.append(right[j])
            j += 1
        return array
    
    def __sort(self, data):
        if (len(data)) <= 1:
            return data

        left_half, right_half = self.__split(data)
        left = self.__sort(left_half)
        right = self.__sort(right_half)
        return self.__merge(left, right)

    def sort(self):
        now = time()
        self.data = self.__sort(self.data)
        print("Took ", time() - now, "s to run")
    

b = MergeSort([3, 5, 1, 50, 4, 23, 45, 56, 4, 5, 8, 11, 23, 12, 34, 134, 234, 11, 23, 123, 4, 25, 64])
b.sort()
print(b.data)
