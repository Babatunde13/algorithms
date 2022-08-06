class LinearSearch:
    def __init__(self, data) -> None:
        self.data = data
    
    def find(self, target):
        for idx in range(len(self.data)):
            if (self.data[idx] > target):
                print("Too high...")
            elif self.data[idx] == target:
                print("Correct...")
                return idx
            else:
                print("Too low...")
        return -1

a = LinearSearch([1, 2, 4, 5, 6, 7, 8, 8, 9, 10])
a.find(2)
